class Solution(object):
    def addTwoNumbers(self, l1, l2):
        zero = 1
        lsum = 0
        while l1:
            lsum += l1.val * zero
            zero *= 10
            l1 = l1.next
        zero = 1
        while l2:
            lsum += l2.val * zero
            zero *= 10
            l2 = l2.next
        
        if lsum == 0:
            return ListNode(0)

        dummy = ListNode(0)
        current = dummy

        while lsum > 0:
            digit = lsum % 10
            current.next = ListNode(digit)
            current = current.next
            lsum = lsum // 10
        return dummy.next
