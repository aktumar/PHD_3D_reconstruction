# FORMULATIONS IN PAPER

<a name="form1"/>

##### [1] 3D ShapeNets: A Deep Representation for Volumetric Shapes

1) Энергия сверточного слоя *E* для этой модели может быть вычислена как : 

<img src="https://latex.codecogs.com/svg.latex?E(v,h)&space;=&space;-\sum_f\sum_j(h_j^f(W^f*v)_j&plus;c^fh^f_j)-\sum_lb_lv_l" title="E(v,h) = -\sum_f\sum_j(h_j^f(W^f*v)_j+c^fh^f_j)-\sum_lb_lv_l" />

- v_l - каждый видимый элемент
- h^f_j - каждый скрытый элемент в функцианальном канале f
- W^f - сверточный фильтр
- ∗ - означает операцию свертки

В этом определении энергии каждая видимая единица v_l связана с уникальным членом смещения b_l, чтобы облегчить реконструкцию, и все скрытые единицы {h^f_j} в одном канале свертки имеют один и тот же член смещения c^f.
