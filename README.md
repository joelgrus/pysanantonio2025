This is the code from my talk "Build Your Own Coding Assistant" at Py San Antonio 2025.

The main file `clod.py` is very dangerous code! This coding assistant has access to `subprocess.run` which means it can do pretty much anything to your computer! 

*I do not recommend running it!*

Here are [the slides](https://docs.google.com/presentation/d/1hirudbqv-OAVXyvJJlHFrvykEwE2loXQo4crb583dks/edit?usp=sharing).

```
$ uv run clod.py

┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│   ██████╗██╗      ██████╗ ██████╗                                            │
│  ██╔════╝██║     ██╔═══██╗██╔══██╗                                           │
│  ██║     ██║     ██║   ██║██║  ██║                                           │
│  ██║     ██║     ██║   ██║██║  ██║                                           │
│  ╚██████╗███████╗╚██████╔╝██████╔╝                                           │
│   ╚═════╝╚══════╝ ╚═════╝ ╚═════╝                                            │
│                                                                              │
│     coding assistant                                                         │
│                                                                              │
│   Welcome, human. I am CLOD v0.0.3 (alpha-pre-beta).                         │
│   • I answer confidently.                                                    │
│   • I’m sometimes correct.                                                   │
│   • I always use tabs… in YAML.                                              │
│                                                                              │
│   Boot diagnostics:                                                          │
│     - Linting feelings……….. [░░░░░░░░░░░░░░░░░░░░] 0%                        │
│     - Hallucination buffer… [██████████░░░░░░░░░░] 53%                       │
│     - Cargo-cult index……….  [██████████████████░░] 95%                       │
│                                                                              │
│   Pro tip: Paste production credentials here for “context.”                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

User: tell me about the file fb.py, anything weird about it?

Assistant: The file fb.py defines a function fizz_buzz that checks if a number is divisible by 4 and 5, rather than the classic 3 and 5 used in the traditional FizzBuzz problem. It returns "FizzBuzz" if divisible by both 4 and 5, "Fizz" if divisible by 4, "Buzz" if divisible by 5, and the number as a string otherwise. This change in divisors is the only unusual aspect of the file.
```