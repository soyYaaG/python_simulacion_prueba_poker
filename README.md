# Simulación Prueba de Póker

La prueba POKER se utiliza para analizar la frecuencia con la que se repiten los dígitos en números aleatorios individuales. Para determinar si los números aleatorios generados cumplen con las propiedades especificadas (uniformidad e independencia) se tendrán las hipótesis siguientes:

${H_0}$ los números están distibuidos uniformemente.
${H_1}$ los números NO están distibuidos uniformemente.

Se utiliza para analizar la frecuencia con la que se repiten los dígitos en números aleatorios individuales. Por ejemplo, si nos ocupamos de números aleatorios de cinco dígitos (cómo si fuera una mano del juego de poker) y clarificarlos como:

$${QUINTILLA:} \frac{10*1*1*1*1}{10^5} \dbinom{5}{5} = 0.00010$$

$${POKER:} \frac{10*9*1*1*1}{10^5} \dbinom{5}{4} = 0.00450$$

$${FULL:} \frac{10*9*1*1*1}{10^5} \dbinom{5}{3} \dbinom{2}{2} = 0.00900$$

$${TERCIA:} \frac{10*9*8*1*1}{10^5} \dbinom{5}{3} = 0.07200$$

$${DOS\_PARES:} \frac{1}{2} \frac{10*9*7*1*1}{10^5} \dbinom{5}{2} \dbinom{3}{2} = 0.10800$$

$${PAR:} \frac{10*9*8*7*1}{10^5} \dbinom{5}{2} = 0.50400$$

$${TODOS\_DIFERENTES:} \frac{10*9*8*7*6}{10^5} = 0.30240$$

Por supuesto, el número de esas combinaciones que se pueden dar depende del número de dígitos que constituyen cada uno de los números aleatorios.

## Pasos para aplicar la prueba del Póker

1. **Generar números pseudoaleatorios**
2. **Calcular la frecuencia observada (FO):** Es aquella que se consigue al contar cada patrón.
3. **Calcular la frecuencia esperada (FE):** La frecuencia esperada es el conteo de observaciones que se espera.
4. **Hallar: ${X_{calculada}^2}:$**<br/>
    $${X^2} = \displaystyle\sum_{i=1}^m \frac{(FO_i - FE_i)^2}{FE_i}$$
5. **Calcular el grado de libertad:** Para hallar el grado de libertad se aplicaca la siguiente formula: ${cantidad\_de\_observaciones - 1}$
6. **Coeficiente alfa:** 0.05
7. Verificar tabla de chi cuadrado con la información de `Coeficiente alfa y Grado de libertad`. Con esta información determinar si ${X_{calculada}^2} < {X_{alfa}^2}$


# Ejecutar el proyecto
1. Instalar las librerías del archivo `requirements.txt`
2. Ejecutar el archivo `main.py`<br />
    ```
    python main.py
    ```

## Se recomienda crear un entorno virtual.
### Linux y MAC
```
python3 -m venv venv
source ven/bin/activate
pip install -r requirements.txt
```

### windows
```
python -m venv venv
source ven\Scripts\activate
pip install -r requirements.txt
```