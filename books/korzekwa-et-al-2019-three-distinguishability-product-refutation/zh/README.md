# 同一组概率，三个正交态

想象一台机器有四盏灯。无论拨到三个挡位中的哪一个，四盏灯闪烁的比例都是 $1/6,1/4,7/24,7/24$。只看灯，你无法分辨挡位。但量子力学允许另一种测量，把这三个挡位每次都辨认出来。关键是：量子态用**振幅**描述。最初的测量只读出振幅的模平方，看不到相位；相位却可以使两个向量的内积恰好抵消为零。

哪些四项概率能由三个可完美区分的态共同拥有？把所有这样的概率向量组成的集合记作 $\mathcal A_4^3$。严格地说，三个态是迹为一的半正定矩阵，支撑空间两两正交。纯态可以写成 $xx^*$，其中 $x$ 是单位向量；它的对角线就是 $(|x_k|^2)_k$。因此，只要找到三个正交单位向量，且它们每个坐标的模平方都相同，就得到一个例子。相同的模平方让第一种测量无法区分它们；正交性保证另一种测量能够区分。

::: {.film src="001-one-diagonal"}
有理数例子：同一组概率、三个正交态，以及在所有排列中都不通过的二乘二检验。
:::

## 原猜想画出的图形

任何共同对角线都满足 $p_k\le1/3$：三个支撑正交的态之和不超过单位矩阵，故其第 $k$ 个对角元 $3p_k$ 不超过一。加上 $p_k\ge0$ 和 $\sum_k p_k=1$，这些条件围出一个四面体。第 $j$ 个顶点 $f^j$ 的第 $j$ 个分量为零，其余为 $1/3$。设混合四个顶点的权重是 $q_k$，所得向量的第 $k$ 项便是 $(1-q_k)/3$。因此权重没有调整余地：$q_k=1-3p_k$。

Korzekwa、Czachórski、Puchała 与 Życzkowski 在 §III.B 式 (30) 中猜想，每个可实现的 $p$ 都能由两次独立二选一的结果混合而成。例如，两枚硬币出现正面的概率是 $a,b$，那么四种联合结果的权重是 $ab,a(1-b),(1-a)b,(1-a)(1-b)$。现在允许任意安排四种结果与四个顶点的对应关系，甚至每个点都可以换一种排列。这样就能覆盖所有可实现的概率向量吗？

::: {.proposition #rank-one-test mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s2" status="written-proof" proof="pf-rank-one-test" doi="10.5281/zenodo.24406607" source="Proposition 2" request="https://github.com/the-omega-institute/trureturing-requests/issues/592"}
**秩一检验（Ma 与 Zhang，命题 2）。** 若 $0\le p_k\le1/3$ 且 $\sum_k p_k=1$，把剩余权重 $q_k=1-3p_k$ 排成两行 $(u,v)$ 与 $(w,h)$。这一排列有乘积表示，当且仅当 $uh=vw$。若允许任意排列，只需检验三种把四项分成两对的方式。
:::

::: {.proof #pf-rank-one-test}
把两枚硬币给出的四项相乘，立即得到 $uh=vw$。反过来，取第一行总和 $a=u+v$、第一列总和 $b=u+w$，两者都在 $[0,1]$ 中。由于四项总和为一，有 $u-ab=uh-vw$。若行列式为零，就有 $u=ab$；再从行和、列和里减去相应项，得到另外三个乘积。整个推导没做除法，所以零行或零列也适用。考虑所有排列时，与第一项配对的可以是其余任意一项；选定它以后，另一对也随之确定。
:::

## 可以手算的反例

::: {.remark #rational-example mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s5"}
**有理数例子（推论 5）。** $p_*=(1/6,1/4,7/24,7/24)$ 可以实现，但无论怎样排列都没有乘积表示。它到所有乘积形式之并的总变差距离至少是 $1/192$。
:::

要做两项独立检验。先为三个向量都取模长 $(\sqrt{1/6},\sqrt{1/4},\sqrt{7/24},\sqrt{7/24})$，再分别乘上下表的一行相位。相位的模都是一，所以三个向量的模平方仍然都是 $p_*$。

| 向量 | 相位一 | 相位二 | 相位三 | 相位四 |
|---|---|---|---|---|
| 第一个 | $1$ | $1$ | $1$ | $1$ |
| 第二个 | $1$ | $\omega$ | $v$ | $w$ |
| 第三个 | $1$ | $\omega$ | $w$ | $v$ |

取 $\omega=(-1+i\sqrt3)/2$，分别用正负号定义 $v,w=-(1+3i\sqrt3)(1\pm i\sqrt6)/14$。这给出 $v+w=-(1+3i\sqrt3)/7$。第一个向量与另外两个的内积都是 $1/6+\omega/4+(7/24)(v+w)=0$。后两个向量交换了最后两个相位，故相应的内积贡献是实数。利用 $\operatorname{Re}(\overline v w)=-5/7$，得到内积 $1/6+1/4+2(7/24)(-5/7)=0$。

再抛开相位，算出唯一的权重 $(1/2,1/4,1/8,1/8)$。把 $1/2$ 与 $1/4$ 配成一对，两对乘积相差 $1/8-1/64=7/64$；把它和任意一个 $1/8$ 配对，则差为 $1/16-1/32=1/32$。没有零差，因此 **24 种排列全都失败**。最小的差是 $1/32$。把每个乘积差展开，系数的绝对值都不超过一，故从 $q$ 改成 $q'$ 时，配对差改变至多 $\|q-q'\|_1$。乘积点至少有一种配对差为零，并且 $\|q-q'\|_1=3\|p-p'\|_1$。因此总变差距离 $\tfrac12\|p-p'\|_1\ge1/192$。这不是舍入误差。

::: {.remark #edge-family mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s4"}
**中心到边的点族（命题 4）。** 令 $c=(1-3t)/4$，取 $p=(c+st,c+(1-s)t,(1+t)/4,(1+t)/4)$，其中 $0\le s\le1/2$、$0\le t\le1/3$。这些点都有纯态见证（Korzekwa 等，附录 C.1）。若 $s<1/2$ 且 $0<t<1/3$，则所有排列均无法通过乘积检验。
:::

有理数反例取的是 $s=1/4,t=1/6$。一般构造先选第二项的相位，使前两个加权项之和的模为 $\sqrt{t(1+t)}/2$。用后两项抵消它，再交换末两项的相位，即可得到第三个正交态。检验乘积时，四个权重是 $(c+3t(1-s),c+3ts,c,c)$，三种配对差分别是 $3ct+9t^2s(1-s)$ 和两次 $3ct(1-2s)$，在所述范围内均为正。端点也有见证，但这一严格不等式论证并不覆盖端点。$s=0$ 的径向子族早已由 Bengtsson、Ericsson、Kuś、Tadej 与 Życzkowski 给出。

## 另一种反例与结论边界

::: {.remark #interior-example mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s1"}
**族外的反例（定理 1）。** 令 $r=\sqrt5$、$\alpha=(5-r)/10$、$\beta=(5-r)/20$、$\gamma=(r-1)/4$。点 $(\alpha,\beta,\alpha,\gamma)$ 位于四面体严格内部，具有三个纯态见证，却对所有排列及所有 $a,b\in[0,1]$ 都不具乘积形式。
:::

这里相等的两项既非最大也非最小，不像中心到边的点族那样两项同为最大。证明取 $z=e^{\pi i/5}$，三行相位为 $(1,1,1,1)$、$(1,z^2,z^4,z^7)$、$(-1,z^9,z^3,z^9)$。模长仍是各概率的平方根。令 $g=(1+\sqrt5)/2$；由 $z+\overline z=g$ 和 $|z|=1$ 得 $z^2=gz-1$，从而高次幂都能化成常数与 $z$ 的一次项。前两个向量内积的两个系数分别是 $\alpha-\beta-\alpha g+\gamma$ 和 $\beta g+\alpha-\gamma g$，都等于零。其余内积同理消去（定理 1）。三个配对差为 $(21-9r)/10,(33-15r)/40,-(21-9r)/10$，无一为零。

::: {.remark #irrational-distance mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s3"}
**另一个反例的距离（推论 3）。** 最小绝对配对差是 $(15\sqrt5-33)/40$。沿用有理数例子的估计，得到到乘积形式之并的总变差距离下界 $(15\sqrt5-33)/240>0$。
:::

::: {.remark #state-channel-capacity mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s6"}
**态与信道（推论 6）。** 对两个反例中的任一个，将三个向量补成酉矩阵，第四列的模平方就是 $1-3p$。故 $T(p)=(p\ p\ p\ 1-3p)$ 是酉随机矩阵，即某个酉矩阵逐项取模平方的结果。两个反例的共同对角线容量恰好为三：若四维中有四个支撑正交的态，它们必是一组基的纯态，故对角线必均匀。任何含有这样一列的随机矩阵，都允许在固定非纠缠输入上区分至少三个信道；对 $T(p)$ 可区分四个。这不是说有四个态共享 $p$，而是说同一个输入通过不同信道可得到四个正交输出。信道构造是 Korzekwa 等命题 15 与 19 的特例。
:::

::: {.remark #pure-reduction mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s8"}
**这一维数只需纯态见证（命题 8）。** $\mathcal A_4^3$ 中的每个点都有三个纯态见证。因此成员资格等价于 $(p\ p\ p\ 1-3p)$ 的酉随机性；反过来，具有相应模平方的酉矩阵前三列给出见证。
:::

不全是纯态时，三个秩只可能是 $(2,1,1)$ 的某种排列。两个纯态向量在各坐标模长相同，所以可在每个坐标同时乘一个相位，使这两个向量互为共轭；零坐标任选相位。它们的正交补在共轭下不变。将第三个态与其共轭取平均，得到这个二维补空间上的实矩阵，且保留对角线。若实正交单位特征向量为 $a,b$，权重为 $\lambda,1-\lambda$，则 $\sqrt\lambda\,a+i\sqrt{1-\lambda}\,b$ 的模平方里没有交叉项，恰好给出同一对角线。$\lambda=0,1$ 也包括在内。

::: {.remark #face-exclusion mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s7"}
**面内部排除（推论 7；Korzekwa 等，附录 C.2）。** 四面体任一二维面的相对内部都不属于 $\mathcal A_4^3$。这没有排除边和顶点。在这样的面内部，一个分量为 $1/3$，其余三项严格介于零与 $1/3$ 之间；饱和的一行留下二维行空间。相位方程会把三个剩余正权重分为总和相等的两个符号类。其中一类只有一项，该项须占剩余总权重的一半，迫使第二个分量等于 $1/3$。
:::

::: {.remark #radial-endpoint mathesis="collected:korzekwa-et-al-2019-three-distinguishability-product-refutation:2:s9"}
**径向端点（推论 9）。** 对 $-1/9\le t<0$，点 $(1-3t,1+t,1+t,1+t)/4$ 不可实现。此时 $(1-3t)/(1+t)>1$，Bengtsson 等的纯态相位方程无解；上一条将它推广到混合态。$t=0$ 时，傅里叶矩阵的任意三列给出均匀对角线，故不能排除中心点。
:::

## 已知与未知

反例否定了式 (30) 的**必要性**，没有否定充分性，也没有给出整个集合的刻画或解决星形性。公开的 Lean 定理说的是：没有一种**固定**的顶点排列适用于整个区域。证明对所有排列使用同一个无理数反例，但命名定理的结论没有写出严格内部的纯态见证。秩一等价判据及上述其他结论有原文书面证明，不能由这条 Lean 定理一并认定为已形式化。

::: {.slides src="overview"}
英文报告幻灯片与讲稿备注。
:::

**资料来源。** Haobo Ma 与 Wenlin Zhang，[《Counterexamples to Korzekwa et al. (2019)》，第 2 版](https://doi.org/10.5281/zenodo.24406607)。原猜想、中心到边的构造与面排除见 Korzekwa、Czachórski、Puchała 与 Życzkowski，[《Distinguishing classically indistinguishable states and channels》](https://doi.org/10.1088/1751-8121/ab30f7)，§III.B 与附录 C。先前的径向构造与相位障碍见 Bengtsson、Ericsson、Kuś、Tadej 与 Życzkowski，[《Birkhoff's polytope and unistochastic matrices, N = 3 and N = 4》](https://doi.org/10.1007/s00220-005-1392-8)，§4 与附录 C。参与形式化可查看[共享请求](https://github.com/the-omega-institute/trureturing-requests/issues)，再依照[上游贡献指南](https://github.com/the-omega-institute/trureturing/blob/dev/docs/CONTRIBUTING.md)从自己的 fork 提交聚焦的证明。
