# Exact Synthetic Control Method (ESCM)

Written by Veronica Backer-Peral
Email: veronicabp@gmail.com

## Description:

The exact synthetic control method (ESCM) builds upon the seminal work on the synthetic control method (SCM) of Abadie and Gardeazabal (2003) and Abadie, Diamond, and Hainmueller (2006). The primary difference between SCM and ESCM is that ESCM uses an algebraic algorithm first developed by Dines (1926) rather than a numerical approximation algorithm to create the synthetic control. Not only does this produce exact solutions, it also can produce multiple solutions, enabling the researcher to measure the robustness of the synthetic control.

## How to use:

The current program is implemented for a study on what public healthcare would look like in the United States. It uses data from the United Nations, World Health Organization, Organization for Economic Cooperation and Development, and Gallup World Poll.

To run the full program and obtain results, run the command:

```
exact-synthetic-control-method% python3 src/escm.py
```