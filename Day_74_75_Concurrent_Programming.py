"""
Process:
A running Program is known as a process.
For a process to run, it needs memory and CPU.

Thread:
A Light Weight Process.
A Thread is a part of the process.

In programming, a thread is the smallest unit of execution that an operating system can schedule. It represents a single, sequential flow of control within a program. Threads are often referred to as "lightweight processes" because they share resources with other threads within the same process, but each thread maintains its own execution context, including a program counter, register set, and stack.
Key characteristics of threads:
Concurrency: Threads enable a program to perform multiple tasks seemingly simultaneously (on single-core processors through rapid switching, and truly in parallel on multi-core processors). This allows for more efficient resource utilization and improved responsiveness in applications.
Shared resources: Threads within the same process share the process's memory space, including code, data, and operating system resources like open files. This shared access facilitates efficient communication and data exchange between threads.
Independent execution context: Each thread has its own unique execution context, allowing it to execute independently of other threads within the same process.
Lightweight: Compared to processes, threads require fewer resources to create and manage, making them more efficient for achieving concurrency within a single application.
How threads are used in programming:
Multitasking: Threads allow a program to handle multiple tasks concurrently, such as a user interface thread handling user input while a background thread performs data processing.
Responsiveness: By offloading time-consuming operations to separate threads, the main application thread can remain responsive to user interactions.
Parallel computing: On multi-core systems, threads can be used to distribute computational tasks across multiple cores, leading to faster execution times for computationally intensive operations.
Example (conceptual):
Consider a web server application. Instead of handling each client request sequentially, a multithreaded server can create a new thread for each incoming client connection. This allows the server to handle multiple clients concurrently, improving performance and responsiveness.


Thread vs Process:
Thread:
1. Light Weight
2. Shares the memory and CPU.

Process:
1. Heavy Weight
2. Need separate CPU and memory.


Tread vs Process:
A process is a program in execution with its own independent memory space, while a thread is the smallest unit of execution within a process that shares the same memory space as other threads in that process. Processes are heavyweight and take more time and resources to create and switch between, whereas threads are lightweight, making them faster for tasks that require frequent communication and synchronization within the same application.
Process
Definition: An instance of a program running on a computer.
Memory: Each process has its own separate memory space, which includes code, data, and heap.
Communication: Communication between processes (Inter-Process Communication or IPC) is slower and more complex because it requires the operating system to manage the data transfer between separate memory spaces.
Resource Usage: Processes are considered "heavyweight" because they consume more memory and system resources.
Fault Tolerance: Processes are isolated from each other. An error in one process will not typically affect another process.
Example: Opening a web browser is one process, and running a different application like a word processor is a separate process.
This video explains the difference between a process and a thread in simple terms:

Thread
Definition: A segment of a process, or the smallest unit of execution that can be scheduled.
Memory: Threads within the same process share the same memory space, including the code, data, and heap. However, each thread has its own program counter, register set, and stack.
Communication: Communication between threads is faster and more efficient because they can access shared data directly.
Resource Usage: Threads are "lightweight" and use fewer resources than processes. Creating and switching between threads is much faster than for processes.
Fault Tolerance: Threads are less fault-tolerant. An error in one thread can potentially crash the entire process because they share memory.
Example: In a web browser (the process), each tab can be a different thread, allowing you to scroll a page while another page is loading.


References:
geeksforgeeks.org/operating-systems/difference-between-process-and-thread/


Python is a Single Threaded Programming Language.
"""
import requests
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def download_image(image_url, file_basename, count):
    response = requests.get(image_url)
    filename = file_basename + str(count) + ".png"
    with open(filename, "wb") as fp:
        fp.write(response.content)

def download_image_using_multithreading(image_url, filename):
    response = requests.get(image_url)
    with open(filename, "wb") as fp:
        fp.write(response.content)


image_urls = ["https://media.istockphoto.com/id/1317323736/photo/a-view-up-into-the-trees-direction-sky.jpg?s=2048x2048&w=is&k=20&c=oo7SGfjmPkybpqoNccDsYWG-4uxSmn8G79NiLA1mNvs=",
              "https://media.istockphoto.com/id/1419410282/photo/silent-forest-in-spring-with-beautiful-bright-sun-rays.jpg?s=2048x2048&w=is&k=20&c=t9_zg20wVbrBoGn0tw__1fFq4ykeKs15TQQ3x-ehVC0=",
              "https://cdn.pixabay.com/photo/2022/08/08/19/36/landscape-7373484_1280.jpg",
              "https://cdn.pixabay.com/photo/2022/04/15/07/58/sunset-7133867_1280.jpg",
              "https://cdn.pixabay.com/photo/2022/11/27/13/22/tree-7619791_1280.jpg",
              "https://cdn.pixabay.com/photo/2022/05/10/14/37/glacier-7187291_1280.jpg",
              "https://cdn.pixabay.com/photo/2024/12/28/03/39/field-9295186_1280.jpg",
              "https://cdn.pixabay.com/photo/2014/09/02/15/28/styggkarret-433688_1280.jpg",
              "https://cdn.pixabay.com/photo/2022/11/05/19/56/bachalpsee-7572681_1280.jpg",
              "https://cdn.pixabay.com/photo/2020/04/22/08/06/dolomites-5076487_1280.jpg",
              "https://cdn.pixabay.com/photo/2024/11/17/04/52/chilli-9202873_1280.jpg",
              "https://cdn.pixabay.com/photo/2017/08/16/01/23/desert-2646209_1280.jpg"
              ]
file_basename = ".\\Images\\image"
count = 0

"""
t1 = time.time()
for image_url in image_urls:
    download_image(image_url, file_basename, count)
    count += 1
t2 = time.time()
print("Total Time Taken for downloading images: ", (t2 - t1))
"""


filenames = [".\\Images\\image1.png", ".\\Images\\image2.png", ".\\Images\\image3.png", ".\\Images\\image4.png",
             ".\\Images\\image5.png", ".\\Images\\image6.png", ".\\Images\\image7.png", ".\\Images\\image8.png",
             ".\\Images\\image9.png", ".\\Images\\image10.png", ".\\Images\\image11.png", ".\\Images\\image12.png",
             ".\\Images\\image13.png", ".\\Images\\image14.png", ".\\Images\\image15.png", ".\\Images\\image16.png"]
t1 = time.time()
with ThreadPoolExecutor(max_workers=12) as executor:
    executor.map(download_image_using_multithreading, image_urls, filenames)
t2 = time.time()
print("Total Time Taken for downloading images: ", (t2 - t1))


"""
with ProcessPoolExecutor(max_workers=10) as executor:
    pass
"""

from concurrent.futures import ProcessPoolExecutor
from time import sleep

values = [3, 4, 5, 6]


def cube(x):
    print(f'Cube of {x}:{x * x * x}')


"""
result = []
with ProcessPoolExecutor(max_workers=5) as exe:
    exe.submit(cube, 2)

    # Maps the method 'cube' with a iterable
    result = exe.map(cube, values)

for r in result:
    print(r)
"""