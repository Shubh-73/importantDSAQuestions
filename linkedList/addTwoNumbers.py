class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> int:
    node1 = l1
    node2 = l2
    final_sum = 0
    power = 0

    while node1 or node2:
        num1 = node1.val if node1 else 0
        num2 = node2.val if node2 else 0
        current_sum = num1 + num2
        final_sum += current_sum + (final_sum * 10)
        #power += 1
        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None

    return final_sum


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    temp1 = l1
    temp2 = l2
    for i in range(1, 6):
        temp1.next = ListNode(i * 3)

        temp2.next = ListNode(5 * i)

        temp1 = temp1.next
        temp2 = temp2.next

    output = addTwoNumbers(l1, l2)
    while l1.next is not None:
        print(f"{l1.val}  +  {l2.val}")
        l1 = l1.next
        l2 = l2.next
    print(output)
