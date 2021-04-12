###Stevens在文章中一共比较了五种IO Model：
- blocking IO    (阻塞IO)
- nonblocking IO (非阻塞IO)
- IO multiplexing (IO多路复用)
- signal driven IO(信号驱动IO)
- asynchronous IO(异步IO)

由signal driven IO（信号驱动IO）在实际中并不常用，所以主要介绍其余四种IO Model。

再说一下IO发生时涉及的对象和步骤。对于一个network IO (这里我们以read举例)，它会涉及到两个系统对象，
一个是调用这个IO的process (or thread)，另一个就是系统内核(kernel)。当一个read操作发生时，该操作会经历两个阶段：
- 1）等待数据准备 (Waiting for the data to be ready)
- 2）将数据从内核拷贝到进程中(Copying the data from the kernel to the process)

###常见的网络阻塞状态
- accept
- recv 
- recvfrom
