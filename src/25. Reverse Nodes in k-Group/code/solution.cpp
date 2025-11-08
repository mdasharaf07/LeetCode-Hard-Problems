class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        
        ListNode* temp = head;
        int count = 0;
        while(temp!=NULL && count<k)
        {
            count++;
            temp = temp->next;
        }

        int i = 0;
        if(count==k)
        {
            ListNode* prev = NULL;
            ListNode* curr = head;
            ListNode* forward = NULL;

            while(i<k){
                forward = curr->next;
                curr->next = prev;
                prev = curr;
                curr = forward;
                i++;
            }

            ListNode* recKahead = reverseKGroup(forward,k);
            head->next = recKahead;
            return prev;

        }
        else
        {
            return head;
        }
    }
};