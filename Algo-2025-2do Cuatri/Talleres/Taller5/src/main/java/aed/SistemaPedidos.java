
public class SistemaPedidos {
    private ABB<Pedido> pedidosPorId;
    private ListaEnlazada<EntradaPedido> pedidosPorLlegada;

    private class EntradaPedido {
        Pedido pedido;
        ABB<Pedido>.HandleABB handle; 

        EntradaPedido(Pedido p, ABB<Pedido>.HandleABB h) {
            this.pedido = p;
            this.handle = h;
        }
    }

    

    public SistemaPedidos(){
        this.pedidosPorId = new ABB<Pedido>();
        this.pedidosPorLlegada = new ListaEnlazada<EntradaPedido>();
    }

    public void agregarPedido(Pedido pedido){
        ABB<Pedido>.HandleABB handle = this.pedidosPorId.insertar(pedido);
        EntradaPedido nuevaEntrada = new EntradaPedido(pedido, handle);
        this.pedidosPorLlegada.agregarAtras(nuevaEntrada);
    }

    public Pedido proximoPedido(){
        if (this.pedidosPorLlegada.longitud() == 0) {
            return null;
        }
        
        EntradaPedido proximaEntrada = this.pedidosPorLlegada.obtener(0);
        this.pedidosPorLlegada.eliminar(0);
        proximaEntrada.handle.eliminar();
        
        return proximaEntrada.pedido;
    }

    public Pedido pedidoMenorId(){
        if (this.pedidosPorId.cardinal() == 0) {
            return null;
        }
        return this.pedidosPorId.minimo();
    }

    public String obtenerPedidosEnOrdenDeLlegada(){
        StringBuffer sb = new StringBuffer("["); 

        ListaEnlazada<EntradaPedido>.ListaIterador iter = this.pedidosPorLlegada.iterador();
        
        while (iter.haySiguiente()) {
            EntradaPedido entrada = iter.siguiente(); 
            sb.append(entrada.pedido.toString()); 
            if (iter.haySiguiente()) {
                sb.append(", ");
            }
        }
        
        sb.append("]");
        return sb.toString();
    }

    public String obtenerPedidosOrdenadosPorId(){
        StringBuffer sb = new StringBuffer("{"); 
        
        ABB<Pedido>.ABB_Iterador iter = this.pedidosPorId.iterador();
        
        while (iter.haySiguiente()) {
            sb.append(iter.siguiente().toString());
            if (iter.haySiguiente()) {
                sb.append(", ");
            }
        }
        
        sb.append("}");
        return sb.toString();
    }}