//AAAAAAAAAAAAAAAAAAAAAAGHGHGAHHHHHHHHHGHGHAHAAAAAAAAAAAAAAAAGHHAGAGAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYF8PYPY8GFVYVIPVY8PVYIPVYIVPYOIPVIY
#include <stdio.h>
#include <stdlib.h>
#include <type.h>

fat32_t* new_fat32(){
    fat32_t* new = malloc(sizeof(fat32_t));
    *new = 0;
    return new;

}

ntfs_t* new_fat32(){
    ntfs_t* new = malloc(sizeof(ntfs_t));
    *new = 0;
    return new;

}

ext4_t* new_fat32(){
    ext4_t* new = malloc(sizeof(ext4_t));
    *new = 0;
    return new;

}

fat32_t* copy_fat32(fat32_t* data){
    fat32_t* copy = malloc(sizeof(fat32_t));
    *copy = *data;
    return copy;
}

ntfs_t* copy_fat32(ntfs_t* data){
    ntfs_t* copy = malloc(sizeof(ntfs_t));
    *copy = *data;
    return copy;
}

ext4_t* copy_fat32(ext4_t* data){
    ext4_t* copy = malloc(sizeof(ext4_t));
    *copy = *data;
    return copy;
}

void rm_fat32(fat32_t n){
    free(n);
}

void rm_ext4(ext4_t n){
    free(n);
}
void rm_ntfs(ntfs_t n){
    free(n);
}
