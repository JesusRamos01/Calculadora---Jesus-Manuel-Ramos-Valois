# RESPUESTAS

1. **Diferencia entre CI y CD:**

	- CI (Integracion Continua) es cuando revisamos automaticamente el codigo cada vez que subimos algo, para ver si todo funciona y pasa las pruebas.

    - CD (Entrega Continua) es cuando despues de eso, el codigo esta listo para que se use, para subir a produccion.

2. **Lenguaje, linter y herramienta de cobertura:**

	- Use Python porque es mas facil y estoy aprendiendo (asi que practico un poco). El linter es flake8 porque nos ayuda a ver errores de estilo. La herramienta de cobertura es coverage porque nos dice que tanto del codigo se prueba.

3. **Umbral minimo de cobertura:**

	- Elegimos 80% porque asi nos aseguramos que la mayoria del codigo esta cubierto por pruebas, pero tampoco es tan difícil de alcanzar.

## Como ver los fallos en los logs

## Run fallido

Cuando algo falla, el workflow se para y sale en rojo. Por ejemplo si pones un error en el codigo, el linter lo detecta y no sigue. Si una prueba no pasa, sale FAILED y no sigue. Si la cobertura es menos de 80%, sale "el coverage es muy bajo" y no sigue.

## Run exitoso

Cuando todo esta bien, el workflow termina y sale en verde. Los logs dicen que todo paso y la cobertura es suficiente.

## Diferencia
La diferencia es que el run exitoso termina y dice que todo ok, el fallido se para y te dice donde estuvo el error.
