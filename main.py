M = int(input("Digite la cantidad de piezas a comprar: "))
i = int(input("Digite el precio unitario: "))
c = M*i

if c > 500000:
    h = c * 0.55
    e = c * 0.3
    ll = c - (h+e)
    C = ll * 0.2
    a = ll + C
    print(f'El monto total de la compra es de: {c}')
    print(f'La inversión de la empresa debe ser de: {h}')
    print(f'El prestamo del banco debe ser de: {e}')
    print(f'El credito a solicitar al fabricante (con el 20% aplicado) debe ser de: {a}')

else:
    r = c * 0.7
    o = c * 0.3
    l = o * 0.2
    i = l + o
    print(f'El monto total de la compra es de: {c}')
    print(f'La inversión de la empresa debe ser de: {r}')
    print(f'El credito a solicitar al fabricante (con el 20% aplicado) debe ser de: {i}')
