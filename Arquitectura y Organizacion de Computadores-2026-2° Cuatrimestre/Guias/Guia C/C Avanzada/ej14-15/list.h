#include "type.h"
#include <stdint.h>

typedef struct node {
void* data;
struct node* next;
} node_t;


typedef struct list {
type_t type;
uint8_t size;
node_t* first;
} list_t;