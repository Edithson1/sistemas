#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file = fopen("generated_data.csv", "r");
    if (file == NULL) {
        printf("No se pudo abrir el archivo\n");
        return 1;
    }

    // Variables para almacenar la suma de cada columna
    float sum_col1 = 0.0, sum_col2 = 0.0, sum_col3 = 0.0;

    // Leer los datos del archivo y calcular la suma
    char line[256];
    while (fgets(line, sizeof(line), file)) {
        float col1, col2, col3;
        sscanf(line, "%f,%f,%f", &col1, &col2, &col3);
        sum_col1 += col1;
        sum_col2 += col2;
        sum_col3 += col3;
    }
    fclose(file);

    // Guardar las sumas en un archivo
    FILE *sum_file = fopen("sums.txt", "w");
    if (sum_file == NULL) {
        printf("No se pudo abrir el archivo para escribir las sumas\n");
        return 1;
    }
    fprintf(sum_file, "Sum_col1: %f\nSum_col2: %f\nSum_col3: %f\n", sum_col1, sum_col2, sum_col3);
    fclose(sum_file);

    return 0;
}
