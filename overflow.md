```sh
$ rustc overflow.rs 
error: this arithmetic operation will overflow
 --> overflow.rs:3:20
  |
3 |     println!("{}", x * x);
  |                    ^^^^^ attempt to compute `300_u16 * 300_u16`, which would overflow
  |
  = note: `#[deny(arithmetic_overflow)]` on by default

error: aborting due to 1 previous error

```
