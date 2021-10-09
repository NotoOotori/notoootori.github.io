---
title: Weak Topology as Colimit
tags: Topology Category-Theory
description: In this article, we will explain the understanding of weak topology as a certain colimit.
---

**Definition.** Let $$X$$ be a set and let a collection $$\{X_{\lambda}\}_{\lambda\in \Lambda}$$ of topological spaces be a cover of $$X$$. Define a topology on $$X$$ by declaring a subset $$F\subseteq X$$ to be closed if and only if $$F \cap X_\lambda$$ is closed in $$X_\lambda$$ for each $$\lambda$$. Name the topology by the weak topology on X.

<br>

We claim that by substituting every occurrence of the word "closed" by "open" in the previous definition, we still obtain the same topology.

**Proposition.** A subset $$E\subseteq X$$ is open in $$X$$ if and only if $$E\cap X_\lambda$$ is open in $$X_\lambda$$ for each $$\lambda$$.

*Proof.* We shall frequently make use of the equation $$(X\backslash E) \cap X_\lambda = X_\lambda \backslash (E\cap X_\lambda)$$.

Suppose $$E\subseteq X$$ is open in $$X$$. Then $$X\backslash E$$ is closed in $$X$$. Thus $$X_\lambda\backslash (E\cap X_\lambda) = (X\backslash E)\cap X_\lambda$$ is closed in $$X_\lambda$$ by definition of weak topology. It implies that $$E\cap X_\lambda$$ is open in $$X_\lambda$$.

Conversely, let $$E\cap X_\lambda$$ be open in $$X_\lambda$$ for each $$\lambda$$. Then $$(X\backslash E) \cap X_\lambda = X_\lambda \backslash (E\cap X_\lambda)$$ is closed in $$X_\lambda$$ for every $$\lambda$$. Again by definition of weak topology we obtain that $$X\backslash E$$ is closed in $$X$$. Thus $$E$$ is open in $$X$$.

<br>

Weak topology on $$X$$ can also be constructed by "gluing" the spaces $$\{X_\lambda\}$$. More precisely, we have the following proposition.

**Proposition.** $$X$$ is the colimit of the full diagram compromised by the spaces $$X_\lambda$$ and the inclusions of their pairwise intersections $$X_\lambda\cap X_{\lambda'}$$.

*Proof.* The information of a cone under the diagram with nadir $$Y$$ consists of a collection $$\{\phi_\lambda\colon X_\lambda \to Y\}$$ of continuous maps satisfying that $$\phi_\lambda$$ and $$\phi_{\lambda'}$$ coincide on $$X_\lambda\cap X_{\lambda'}$$ for every $$\lambda, \lambda'\in \Lambda$$. Then we can glue these maps to obtain a unique map $$\phi\colon X\to Y$$. We shall prove that $$\phi$$ is continuous.

Let $$V\subseteq Y$$ be an open set of $$Y$$. Then $$\phi^{-1}(V)\cap X_\lambda=\phi_\lambda^{-1}(V)$$ is open in $$X_\lambda$$ for every $$\lambda$$. It implies that $$\phi^{-1}(V)$$ is open in $$X$$, which ends the proof.

<br>

Now a natural question arises that whether the weak topology defined by a cover of a topological space is the same as the original one.

**Proposition.** Let $$X$$ be a topological space and let a collection $$\{X_\lambda\}$$ of subspaces be a cover of $$X$$. If either of these statements is true:

1. $$\{X_\lambda\}$$ is an open cover;
2. $$\{X_\lambda\}$$ is a locally finite closed cover, i.e. every $$X_\lambda$$ is closed, and for every element $$x\in X$$ there is a neighbourhood $$U_x\ni x$$ such that $$U$$ intersects only a finite number of $$X_\lambda$$;

then the weak topology of $$X$$ with respect to the cover $$\{X_\lambda\}$$ coincides with the origin topology of $$X$$.

*Proof.* The case of statement 1 is obvious. So we jump to the case of statement 2. By the Axiom of Choice, the $$\{U_x\}$$ in the definition of a locally finite cover forms an open cover of $$X$$. Suppose a subset $$F\subseteq X$$ is closed under the weak topology. It suffices to prove that $$F\cap U_x$$ is closed in $$U_x$$ with subspace topology inherited from $$X$$ for each $$x$$. Let $$U_x = \bigcup_{j=1}^n (F_j\cap U_x)$$, where $$F_j$$ is closed in $$X$$. Then $$F\cap U_x=\bigcup_{j=1}^n((F\cap F_j)\cap U_x)$$ is closed in $$U_x$$, being a finite union of closed subsets. It ends the proof.
