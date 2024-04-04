#include "lists.h"

/**
 * check_cycle - Detects cycles in a singly linked list.
 * @list: represents a pointer to the beginning of the node
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list) {
  listint_t *current, *check;

  if (list == NULL || list->next == NULL)
    return (0);
  current = list;
  check = current->next;

  while (current != NULL && check->next != NULL && check->next->next != NULL) {
    if (current == check)
      return (1);
    current = current->next;
    check = check->next->next;
  }
  return (0);
}
