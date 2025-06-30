# Trait

## Blanket implementations

implementations of a trait on any type that satisfies the trait bounds are called blanket implementations and are use extensively in the rust standard library. For example, the standard library implements the `ToString` trait on any type that implements the `Display` trait. The `impl` block in the standard library looks similar to this code:

```rust
impl <T: Display> ToString for T {}
```
