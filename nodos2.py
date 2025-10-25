class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print("     Customer:", self.get_customer())
        print("     Quantity:", self.get_qtty())
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class Nodo:
    def __init__(self, order):
        self.order = order
        self.siguiente = None  


class OrderQueue:
    def __init__(self):
        self.head = None  
        self.tail = None  

    def add_order(self, order):
        nuevo_nodo = Nodo(order)
        if self.head is None:
            self.head = nuevo_nodo
            self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            self.tail = nuevo_nodo

        print(f"Pedido agregado para el cliente: {order.get_customer()}")

    def process_next_order(self):
        if self.head is None:
            print("No hay pedidos pendientes para procesar.")
        else:
            siguiente_pedido = self.head.order
            print("Procesando pedido:")
            siguiente_pedido.print()

            self.head = self.head.siguiente

            if self.head is None:
                self.tail = None

    def show_all_orders(self):
        if self.head is None:
            print("No hay pedidos en la cola.")
        else:
            print("Pedidos en la cola:")
            actual = self.head
            while actual is not None:
                actual.order.print()
                actual = actual.siguiente


if __name__ == "__main__":
    order_queue = OrderQueue()

    order1 = Order(10, "Cliente A")
    order2 = Order(5, "Cliente B")
    order3 = Order(20, "Cliente C")

    order_queue.add_order(order1)
    order_queue.add_order(order2)
    order_queue.add_order(order3)

    order_queue.show_all_orders()

    order_queue.process_next_order()
    order_queue.process_next_order()
    order_queue.process_next_order()

    order_queue.process_next_order()
