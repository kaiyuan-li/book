# Tokio

## Q n A 

1. What does `Send` mean? `Send` means that when `.await` suspends the thread, the result can be moved to another thread (the caller thread). `Rc`is a type that cannot be `Send`. `Sync` means a type can be concurrently accessed through immutable references. `Cell` is `Send` but not `Sync` because it can be modified through an immutable reference.
1. What's the benefit of `bytes::Bytes` over `Vec<u8>`? `clone()` on `Bytes` does not clone the data. It is roughly an `Arc<Vec<u8>>`.
1. Difference between sync mutex `std::sync::Mutex` and async mutext `tokio::sync::Mutex`? Sync mutex will block current thread while waiting but async mutex won't.
1. The problem with sync mutex is that when multiple threads are contending (i.e. competing) for a mutex, only one will be working while others are all waiting. To solve this problem:
  1. Switching to a dedicated task to manage state and use message passing
  1. shard the mutex
  1. restructure code to avoid mutex
1. Sending with oneshot channel does not require await. Result of success or failure is known immediately.
1. rust async functions are state machines. It will check the contained future's `poll()` and decide if go to the next state, or check back later.

## Stream

Follow this [tutorial](https://tokio.rs/tokio/tutorial/streams) to learn how to create a stream. Especially the implementation of [`into_stream()`](https://docs.rs/mini-redis/0.4.1/src/mini_redis/client.rs.html#398-408)
