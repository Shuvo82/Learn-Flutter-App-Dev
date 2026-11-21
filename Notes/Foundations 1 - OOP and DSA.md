# Foundations 1 — OOP + Data Structures & Algorithms

Read Part 1, then Part 2, then do the **practice at the end** in writing. Examples are in Dart; in an exam, any language is usually accepted.

---

# Part 1 — Object-Oriented Programming (OOP)

## 1.1 Class and Object
- **Class**: a **blueprint** that defines properties (fields) and behaviour (methods).
- **Object**: an **instance** of a class, a real thing in memory created from the blueprint.

```dart
class Student {              // class = blueprint
  String name;
  int roll;
  Student(this.name, this.roll);   // constructor
  void show() => print('$name - $roll');
}
final s = Student('Rahim', 10);   // object = instance
```

**Constructor**: a special method that runs when an object is created; it initializes fields. Types: default, parameterized, named (`Student.guest()`), copy.

## 1.2 The 4 Pillars of OOP (asked very often)

| Pillar | One-line definition | Example |
|---|---|---|
| **Encapsulation** | Bundle data + methods in a class and **hide data** using access control | private `_balance` + `deposit()` |
| **Abstraction** | Show **what** an object does, hide **how** | abstract `Shape.area()` |
| **Inheritance** | A child class **acquires** properties/methods of a parent class (**IS-A** relation) | `Dog extends Animal` |
| **Polymorphism** | **One interface, many forms**: the same method call behaves differently | `shape.area()` works for Circle and Square |

```dart
// Encapsulation
class BankAccount {
  double _balance = 0;                  // private (Dart: underscore)
  double get balance => _balance;       // read-only access
  void deposit(double amt) { if (amt > 0) _balance += amt; }
}

// Abstraction + Inheritance + Polymorphism
abstract class Shape { double area(); }               // abstraction
class Circle extends Shape {                          // inheritance
  final double r; Circle(this.r);
  @override double area() => 3.1416 * r * r;          // overriding
}
class Square extends Shape {
  final double a; Square(this.a);
  @override double area() => a * a;
}
void main() {
  List<Shape> shapes = [Circle(2), Square(3)];
  for (final s in shapes) print(s.area());            // polymorphism
}
```

## 1.3 Types of Polymorphism
| Compile-time (static) | Run-time (dynamic) |
|---|---|
| **Method overloading**: same name, **different parameters**, in the same class | **Method overriding**: child class **redefines** a parent method with the **same signature** |
| Decided by the compiler | Decided at runtime (dynamic dispatch) |
| Java/C++ support it; **Dart does not** (it uses optional/named params instead) | `@override` in Dart/Java |

## 1.4 Types of Inheritance
Single (A→B), Multilevel (A→B→C), Hierarchical (A→B, A→C), Multiple (A,B→C), Hybrid.
- **Java and Dart do not allow multiple inheritance of classes** (because of the **diamond problem**); they allow multiple **interfaces** (Dart: `implements`, plus **mixins** with `with`).

## 1.5 Abstract Class vs Interface
| Abstract class | Interface |
|---|---|
| Can have **both** abstract and concrete methods | (Classic) only method **signatures** |
| Can have fields/constructor | No state (Java: only constants) |
| A class **extends one** | A class can **implement many** |
| Use for **IS-A** with shared code | Use for a **capability/contract** ("can-do") |

Dart: every class is an implicit interface; `implements` forces you to override everything.

## 1.6 Other OOP terms (short-question favourites)
- **Access modifiers** (Java): `public`, `private`, `protected`, default (package). Dart: `_name` = library-private.
- **Static member**: belongs to the **class**, not to an object (`Math.pi`).
- **`this`**: refers to the current object. **`super`**: refers to the parent class.
- **Association / Aggregation / Composition**: "HAS-A" relations. Aggregation is **weak** (Department has Teachers; teachers exist without it). Composition is **strong** (House has Rooms; rooms die with the house).
- **Coupling** (dependency between classes) should be **low**; **cohesion** (focus within a class) should be **high**.

## 1.7 SOLID Principles (very common in IT exams)
| | Principle | Meaning |
|---|---|---|
| **S** | Single Responsibility | A class should have **one reason to change** |
| **O** | Open/Closed | **Open for extension, closed for modification** |
| **L** | Liskov Substitution | A child object must be usable **wherever the parent is** without breaking it |
| **I** | Interface Segregation | Many **small specific interfaces** rather than one fat interface |
| **D** | Dependency Inversion | Depend on **abstractions**, not concrete classes (inject dependencies) |

*Flutter link:* the Repository pattern + dependency injection (GetX `Get.put`, Provider) = **D**. Splitting UI / controller / repository = **S**.

---

# Part 2 — Data Structures & Algorithms

## 2.1 Big-O (time complexity)
How the running time **grows** as input size *n* grows (worst case).

| Big-O | Name | Example |
|---|---|---|
| O(1) | Constant | Array index access, hash map lookup (average) |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search, one loop |
| O(n log n) | Linearithmic | Merge sort, quick sort (avg), heap sort |
| O(n²) | Quadratic | Bubble/selection/insertion sort, nested loops |
| O(2ⁿ) | Exponential | Naive recursive Fibonacci |

Order: **1 < log n < n < n log n < n² < 2ⁿ < n!**
**Space complexity** = extra memory used.

## 2.2 Linear Data Structures

### Array
Fixed-size, **contiguous** memory, same type. Access by index **O(1)**; insert/delete in the middle **O(n)** (shifting).

### Linked List
Nodes, each with **data + pointer to next**. Types: singly, doubly (prev + next), circular.
| | Array | Linked List |
|---|---|---|
| Memory | Contiguous | Scattered (nodes) |
| Size | Fixed (static) | Dynamic |
| Access i-th | **O(1)** | **O(n)** |
| Insert/delete at front | O(n) | **O(1)** |
| Extra memory | None | Pointer per node |

### Stack: **LIFO** (Last In, First Out)
Operations: `push`, `pop`, `peek`, all **O(1)**.
Uses: function **call stack**, **undo**, expression evaluation, **bracket matching**, browser back button, **Flutter Navigator** (push/pop screens!).

### Queue: **FIFO** (First In, First Out)
Operations: `enqueue` (rear), `dequeue` (front), **O(1)**.
Types: circular queue, **priority queue** (served by priority, usually a heap), **deque** (both ends).
Uses: printer jobs, CPU scheduling, **BFS**, message queues, **an offline sync outbox**.

## 2.3 Hash Table (HashMap / Dart `Map`)
Stores **key → value**. A **hash function** converts the key into an array index. Average **O(1)** insert/search/delete; worst **O(n)** with many collisions.
**Collision** = two keys hash to the same index. Fixed by:
- **Chaining**: each bucket holds a linked list.
- **Open addressing**: probe for the next free slot (linear/quadratic probing).

## 2.4 Non-Linear: Trees
- **Tree**: hierarchical; root, parent, child, leaf, height. (*The Flutter widget tree is a tree!*)
- **Binary tree**: each node has ≤ 2 children.
- **Binary Search Tree (BST)**: left < node < right. Search/insert **O(log n)** average, **O(n)** worst (skewed). Balanced versions: **AVL, Red-Black**.
- **Heap**: complete binary tree; **max-heap** (parent ≥ children) / **min-heap**. Used for priority queues and heap sort.
- **Traversals** (know these orders):
  - **Inorder** (Left, Root, Right): gives **sorted** order for a BST
  - **Preorder** (Root, Left, Right)
  - **Postorder** (Left, Right, Root)
  - **Level order** (BFS, with a queue)

```
        8
       / \
      3   10
     / \    \
    1   6    14
Inorder:   1 3 6 8 10 14
Preorder:  8 3 1 6 10 14
Postorder: 1 6 3 14 10 8
```

## 2.5 Graphs
Vertices (nodes) + edges. Directed/undirected, weighted/unweighted.
Representation: **adjacency matrix** (V×V, O(V²) space) or **adjacency list** (O(V+E), better for sparse graphs).
- **BFS** (Breadth-First Search): level by level, uses a **queue**; finds the **shortest path in unweighted** graphs.
- **DFS** (Depth-First Search): goes deep first, uses a **stack/recursion**; for cycle detection and topological sort.
- **Dijkstra**: shortest path with **non-negative weights** (e.g. maps/routing).

## 2.6 Searching
| Algorithm | Requirement | Time |
|---|---|---|
| Linear search | none | O(n) |
| Binary search | **sorted** + random access | **O(log n)** |

```dart
int binarySearch(List<int> a, int target) {
  int low = 0, high = a.length - 1;
  while (low <= high) {
    int mid = low + (high - low) ~/ 2;   // avoids overflow
    if (a[mid] == target) return mid;
    if (a[mid] < target) low = mid + 1; else high = mid - 1;
  }
  return -1;   // not found
}
```

## 2.7 Sorting (memorize this table)
| Algorithm | Best | Average | Worst | Space | Stable? | Idea |
|---|---|---|---|---|---|---|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Swap adjacent pairs; largest "bubbles" to the end |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Pick the minimum, put it in front |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Insert each item into the sorted left part (good for nearly sorted data) |
| **Merge** | O(n log n) | O(n log n) | O(n log n) | **O(n)** | Yes | **Divide & conquer**: split, sort halves, merge |
| **Quick** | O(n log n) | O(n log n) | **O(n²)** | O(log n) | No | Pick a **pivot**, partition, recurse |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Build a max-heap, extract the max |

**Stable** = equal elements keep their original order.

```dart
// Bubble sort — most commonly asked to write by hand
void bubbleSort(List<int> a) {
  for (int i = 0; i < a.length - 1; i++) {
    bool swapped = false;
    for (int j = 0; j < a.length - 1 - i; j++) {
      if (a[j] > a[j + 1]) {
        final t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
        swapped = true;
      }
    }
    if (!swapped) break;          // already sorted → best case O(n)
  }
}
```

## 2.8 Recursion
A function that **calls itself**. Needs a **base case** (stop condition), or you get a **stack overflow**.
```dart
int factorial(int n) => n <= 1 ? 1 : n * factorial(n - 1);   // O(n)
int fib(int n) => n < 2 ? n : fib(n - 1) + fib(n - 2);       // O(2^n), slow
```
Fix slow recursion with **memoization / dynamic programming** (store results already computed).

## 2.9 Common "write code by hand" questions (practice these)
1. Reverse a string / check **palindrome**
2. **Factorial**, **Fibonacci** (loop and recursive)
3. Check **prime**; print primes up to N
4. **Largest / second largest** in an array
5. **Reverse an array** in place
6. **Bubble sort**, **binary search**
7. Count **vowels** / character frequency (use a Map)
8. **Swap two numbers** without a third variable (`a = a + b; b = a - b; a = a - b;`)
9. **Sum of digits**, reverse a number
10. Remove **duplicates** from a list
11. Check **balanced brackets** using a stack
12. **Reverse a linked list**

---

# Practice — Foundations 1 (answer in writing, then send)

**Section A: short (2 marks each)**
1. Define the four pillars of OOP with one real-life example each.
2. Method overloading vs method overriding.
3. Abstract class vs interface; when would you use each?
4. Why don't Java/Dart allow multiple inheritance of classes? How does Dart get similar reuse?
5. Explain the **S** and **D** of SOLID with an example from a Flutter app.
6. Array vs linked list (at least 3 differences).
7. Stack vs queue, with one real use of each in a mobile app.
8. What is a hash collision? Name two ways to handle it.

**Section B: trees & complexity (6 marks)**

9. Insert into an empty BST in this order: `50, 30, 70, 20, 40, 60, 80`.
   (a) Draw the tree. (b) Write the inorder, preorder and postorder traversals. (c) What's the search time complexity in a balanced vs a skewed BST?

**Section C: code on paper (4 marks each)**

10. Write a function to check whether a string is a **palindrome** (ignore case).
11. Write **binary search** (iterative) and state its time complexity.
12. Write a function that checks whether brackets `()[]{}` in a string are **balanced**, using a stack.

**Section D: sorting (4 marks)**

13. Show each pass of **bubble sort** on `[5, 2, 9, 1, 6]`. Give its best and worst time complexity and say when the best case happens.

Send answers as `1. ... 2. ...`. Partial answers are fine. Write what you know, even if it's just keywords.
