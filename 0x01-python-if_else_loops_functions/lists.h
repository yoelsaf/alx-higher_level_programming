#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
<<<<<<< HEAD
 *
=======
 * for Holberton project
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

<<<<<<< HEAD
#endif /* LISTS_H */
=======
#endif /* LISTS_H */
>>>>>>> 2ec5e458660d8b769d856d9ee079877bc6635f13
