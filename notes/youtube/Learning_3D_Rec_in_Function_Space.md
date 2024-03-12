- COM1 - Исследование нейронных неявных представлений. То что я знала до этого (воксели и облака точек) - плюс сетка(меш) - является традиционной концепцией трехмерного представления явным образом.

  ```mermaid
  graph LR;    
  A[Трехмерное представлние]--> B[Неявным образом];    
  A-->C[Явным образом];    
  C-->D[Воксели];
  C-->E[Облака точек];
  C-->F[Сетка-меш];
  D-->G(Дискретизация пространства в регулярную сетку<br> Легко обрабатывать с помощью нейронных сетей <br>Кубическая память - ограниченное разрешение <br>);
  E-->H(Дискретизация пространства в точки <br>Не моделирует топологию <br>Ограниченное количество точек <br>Глобальное описание)
  F-->I(Дискретизация на вершины и грани<br>Ограниченное количество вершин<br>Нужен шаблон конкретного класса<br>Проблема самопересечения)
  
  B-->J(Нет дискретизации<br>Произвольная топология<br>Маленький объем<br>Не ограничивается классом)
  ```





- COM2 - *Traditional 3D Reconstruction **Pipeline***

  Input Images → Camera poses → Dense Correspondences → 3D reconsruction → Depth Map Fusion → Depth Maps (True image/Ground truth)





- COM3 - *What is a good output representation?*

  <p align="center"><img width="100%" src="https://github.com/aktumar/3D_reconstruction/blob/main/media/Learning_3D_Rec_in_Function_Space.png" /></p>

  
  
  | Voxels                                                       | Points                                   | Meshes                                   |
  | ------------------------------------------------------------ | ---------------------------------------- | ---------------------------------------- |
  | Discretization of 3D space into regular grid                 | Discretization of surface into 3D points | Discretization into vertices and faces   |
  | Easy to process with neural networks                         | Does not model connectivaly / topology   | Limited number of vertices / granularity |
  | Cubic memory O(n^3) - limited resolurion                     | Limited number of points                 | Requires class-specific template - or -  |
  | Manhattan world bias [[12](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/references.md#8)] | Global shape description                 | Leads to self-intersections              |





- COM3 - *About work in video*:

  `Purpose`:

  - Implicit representation - NO discretization
  - Arbitrary topology & resolution
  - Low memory footprint
  - Not restricted to specific class

  `Key idea`:

  - Do not represent 3D shape explicitly
  - Instead, consider surface implicitly as decision boundary of a non-linear classifier
  - [0, 1] - outside/inside





- COM4 - *Training objective*: 

  1. Occupancy network (Формула)

     <p align="center"><img width="100%" src="https://github.com/aktumar/3D_reconstruction/blob/main/media/Learning_3D_Rec_in_Function_Space_2.png" /></p>

     **Multiresolution IsoSurface Extraction (MISE)** - Build octree by incrementally querying the occupancy network. Extract triangular mesh using marching cubes algorithm.

  2. Variational occupancy encoder (Формула)
  
  3. Texture Field. 2D image encoder + 3D shape encoder. GAN discriminator → Adversarial Loss (:mag_right:)





- COM5 - *Representation power*:
  - Ground truth
  - Texture field
  - Voxelization





- COM6 - *Motion*:
  - Extending Occupancy Networks to 4D is hard (curse of dimension)
  - Вместо этого можно представить форму только в один момент времени t = 0
  - Система восстанавливает детали, и лишь затем дает деталям траекторию движения, представляя его непрерывным в пространстве и времени. Это легче, чем представлять весь 4D, из за гладкости представления
  - Логично, в дело вступает взаимосвязь между 3D траекторией и скоростью, представленная в ODE: /--- ds(t)/dt = v(s(t), t) ---/





- COM7 - *Loss Functions:*
  - Reconstruction Loss (:mag_right:)
  - Correspondence Loss (is optional)





- COM8
  - Occupancy Network
  - Convolutional Occupancy Network





- COM9 - *Summary:*
  - Effective output representation for shape, appearence, material, motion, etc
  - No discretization, model arbitrary topology
  - Can be efficiently learned using 2D supervision
  - Many applicaitions: reconstruction, view synthesis, segmentation etc
