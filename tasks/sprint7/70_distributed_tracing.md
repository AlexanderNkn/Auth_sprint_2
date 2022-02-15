### Распределенная трассировка

Добавьте в Auth трасировку и подключите к Jaeger. Для этого вам нужно добавить работу с заголовком x-request-id и отправку трасировок в Jaeger.
*Из коробки библиотека jaeger-client предоставляет контекстный менеджер tracer.start_span(), но это не всегда удобно. Например, вы хотите пометить трасировкой не весь код, а отдельные функции.
Сделайте декоратор @trace для трассировок любых функций.