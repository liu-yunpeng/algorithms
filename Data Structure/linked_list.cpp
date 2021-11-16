#include <iostream>
#include <cstdlib>

// single LinkedList, always add node at head
class Node
{
public:
    Node* next;
    int data;
};

using namespace std;

class LinkedList
{
public:
    Node* head;
    int length;

    LinkedList() {
        this->length = 0;
        this->head = NULL;
    }
    ~LinkedList() {
        std::cout << "list is deleted";
    }

    void add(int data) {
        Node* node = new Node();
        node->data = data;
        node->next = this->head;
        this->head = node;
        this->length++;
    }

    void print() {
        Node* current_node = this->head;
        int i = 1;
        while (current_node) {
            std::cout << current_node->data << "->";
            current_node = current_node->next;
            i++;
        }
        std::cout << "NULL" << std::endl;
    }
};


int main()
{
    LinkedList* list = new LinkedList();
    for (int i = 0; i < 8; ++i)
    {
        list->add(i + 1); // notice the reverse order
    }
    list->print();
    std::cout << "List Length: " << list->length << std::endl;
    delete list;
    return 0;
}