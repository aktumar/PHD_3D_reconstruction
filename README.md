[![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)](https://daringfireball.net/projects/markdown/) 


Небольшое исследование 3D реконструкции (Полезные ссылки, обзор связанных статей и результатов, личные заметки). Начало было положено в августе 2020 года. На создание подобного репо вдохновил - [:mage_man:](https://github.com/timzhang642/3D-Machine-Learning), а на исследование - [:mage_man:](https://www.cs.sfu.ca/~furukawa/) :)​

> Справка:
>
> :mag_right: - WHAT? - Разобрать в ближайшее время
>
> :heavy_division_sign: - Ссылка на формулы из статьи
>
> :thought_balloon: - Объемные заметки
>
> :paperclip: - Эксперименты (Попытки повторить результат)
>
> :ballot_box_with_check: - Изученный материал​
>
> /-..-/ - Переменная или формула
>
> :computer: - Cайт
>
> :space_invader: - GitHub (C++, C, Lua, Python, Jupiter, Cuda, MatLab, Java, notes)
>
> :scroll: - Cтатья
>
> :busts_in_silhouette: - Habr
>
> :clapper: - Видео
>
> [nte] - Ссылка на инфу про этот датасэт указан в этом .md
>
> [doc] - Документация
> 
> [blog] - Блог сайта

## Содержание

- [General Notes](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/general.md)
- [Key words](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/dictionary.md)
- [Models](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/models.md)
- [Papers](#paper)
  - [Survey](#survey)
  - [Datasets](#dataset)
  - [Depth Map](#depthmap)
  - [Lidar](#lidar)
  - [Single image](#singleimage)
  - [Point Clouds](#pointclouds)
  - [Machine learning](#machinelearning)
  - [Texture](#texture)
  - [Real-time 3D reconstruction](#real)
  - [Autonomous Driving](#driving)
- [Others](#others)
  - [Interesting idea](#idea)
  - [Platforms](#platform)
  - [Libraries](#lib)
  - [Youtube channels](#channel)
  - [Devices](#device)
  - [Authors](#authors)
  - [Stackoveflow](#stackoveflow)
  - [Qualified search sites](#news)
  - [Under consideration](#review)


Классная штука, почтиай ---->   https://google.github.io/mediapipe/solutions/objectron.html



<a name="paper" />

## Papers

Подробный анализ прочитанных статей, краткие выводы, результаты.

------

<a name="survey" />

### Survey

Общий обзор на исследование, литературный обзор, ссылки на разные тематические статьи других авторов.

**[[:scroll:](https://vision.cs.princeton.edu/projects/2012/3DnotLow/report.pdf)] (2003 or 2013) 3D reconstruction is not just a low-level task: retrospect and survey**

**[[:scroll:](https://www.researchgate.net/publication/322339391_Algorithms_and_Applications_of_Structure_from_Motion_SFM_A_Survey)] (NOV2017) Algorithms and Applications of Structure from Motion (SFM): A Survey**

**[[:scroll:](https://arxiv.org/pdf/1803.03352v1.pdf)] (2018) Indoor Scene Understanding in 2.5/3D: A Survey**

**[[:scroll:](https://arxiv.org/pdf/1906.06543.pdf)] (NOV2019) Image-based 3D Object Reconstruction: State-of-the-Art and Trends in the Deep Learning Era [[:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/papers/Image_based_3D_Object_Rec_State_of_the_Art.md)]** 

**[[:scroll:](https://arxiv.org/pdf/1906.06113.pdf)] (JUN2019) A Survey on Deep Learning Architectures for Image-based Depth Reconstruction [[:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/papers/A_Survey_on_DLA_for_Imagebased_DepthRec.md)]** 

**[[:scroll:](https://arxiv.org/pdf/2006.02535.pdf)] (JUN2020) A Survey on Deep Learning Techniques for Stereo-based Depth Estimation [[:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/papers/A_Survey_on_DLT_for_Stereo_based_Depth_Estimation.md)]**

**[[:space_invader:/C++/Python](https://github.com/AlexOlsen/DeepWeeds)] DeepWeeds: A Multiclass Weed Species Image Dataset for Deep Learning**

​	↳ **[[:scroll:](https://arxiv.org/pdf/2103.01415v1.pdf)] (MAR2021) A Survey of Deep Learning Techniques for Weed Detection from Images**

**[[:space_invader:/notes](https://github.com/Yochengliu/awesome-point-cloud-analysis#---recent-papers-from-2017)] awesome-point-cloud-analysis**

**[[:space_invader:/notes](https://github.com/timzhang642/3D-Machine-Learning)] 3D-Machine-Learning**

**[[:computer:](https://paperswithcode.com/datasets?mod=rgb-d)] Datasets**



------

<a name="dataset" />

### Datasets

Набор данных для трехмерного машинного обучения

**[[:computer:](https://niessner.github.io/Matterport/)] Matterport3D: Learning from RGB-D Data in Indoor Environments**

​	↳ **[[:space_invader:/C++/C/Lua](https://github.com/niessner/Matterport)] Matterport3D**

​	↳ **[[:scroll:](https://arxiv.org/pdf/1709.06158.pdf)] (SEP2017) Matterport3D: Learning from RGB-D Data in Indoor Environments**

**[[:computer:](https://modelnet.cs.princeton.edu/)] Princeton ModelNet**

**[[:computer:](http://cvlab.hanyang.ac.kr/project/omnistereo/)] Omnidirectional Stereo Dataset**

​	↳ **[[:scroll:](https://sci-hub.se/10.1109/TPAMI.2020.2992497)] (JUN2020) End-to-End Learning for Omnidirectional Stereo Matching with Uncertainty Prior**

ᅠ	↳ **[[:clapper:](https://www.youtube.com/watch?v=R_KJhZd4thg)] (JAN2020) End-to-End Learning for Omnidirectional Stereo Matching with Uncertainty Prior**

​	↳ **[[:scroll:](https://openaccess.thecvf.com/content_ICCV_2019/papers/Won_OmniMVS_End-to-End_Learning_for_Omnidirectional_Stereo_Matching_ICCV_2019_paper.pdf)] (2019) OmniMVS: End-to-End Learning for Omnidirectional Stereo Matching**

ᅠ	↳ **[[:clapper:](https://www.youtube.com/watch?v=6DKen2MQocQ)] (AUG2019) OmniMVS: End-to-End Learning for Omnidirectional Stereo Matching, ICCV 2019**

​	↳ **[[:space_invader:/MatLab/CUDA/C++](https://github.com/hyu-cvlab/sweepnet)] SweepNet**

ᅠ	↳ **[[:scroll:](https://sci-hub.se/10.1109/ICRA.2019.8793823)] (AUG2019) SweepNet: Wide-baseline Omnidirectional Depth Estimation**

ᅠ	↳ **[[:clapper:](https://www.youtube.com/watch?v=7q-NGpuSQYg)] (JAN2019) SweepNet: Wide-baseline Omnidirectional Depth Estimation, ICRA2019**

**[[:computer:](https://cvgl.stanford.edu/projects/objectnet3d/)] ObjectNet3D: A Large Scale Database for 3D Object Recognition**

**[[:computer:](https://shapenet.org)] ShapeNet**





------

<a name="depthmap" />

### Depth Map

Карта глубины, одна из основных глав, над которой я работаю

**[[:scroll:](https://sci-hub.se/10.1109/TCYB.2019.2932005)] (SEP2019) Going From RGB to RGBD Saliency: A Depth-Guided Transformation Model**

**[[:busts_in_silhouette:](https://habr.com/ru/company/top3dshop/blog/511026/)] Обзор программного обеспечения для 3D-сканирования и обработки данных**

**[[:space_invader:/Python](https://github.com/realizator/stereopi-tutorial)] StereoPi tutorial scripts**

​	↳ **[[:busts_in_silhouette:](https://habr.com/ru/post/446872/)] Изучаем OpenCV на StereoPi: карта глубин по видео**

**[[:space_invader:/Java/Python](https://github.com/isl-org/MiDaS)] MiDaS - Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer**

​	↳ **[[:scroll:](https://arxiv.org/pdf/1907.01341v3.pdf)] (AUG2020) Towards Robust Monocular Depth Estimation: Mixing Datasets for Zero-shot Cross-dataset Transfer**

**[[:space_invader:/Python](https://github.com/isl-org/DPT)] DPT - Vision Transformers for Dense Prediction**

​	↳ **[[:scroll:](https://arxiv.org/pdf/2103.13413.pdf)] (MAR2021) Vision Transformers for Dense Prediction**

**[[:computer:](https://rgbd.cs.princeton.edu)] SUN RGB-D: A RGB-D Scene Understanding Benchmark Suite** 

**[[:computer:]([https://rgbd.cs.princeton.edu](https://cs.nyu.edu/~silberman/datasets/nyu_depth_v2.html))] NYU Depth Dataset V2** 

http://stereo.jpn.org/jpn/stphmkr/google/colabe.html

https://3dphoto.io/uploader/

------



<a name="lidar" />

### LIDAR

Обнаружение и определение дальности с помощью света **[[:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/frankenstein/lidar.md)]**

**[[:computer:](https://gistroy.ru/article/lidar/#:~:text=Недостатки%20лидара&text=Стоимость%20лидара%20достаточно%20высока.,результаты%20в%20турбулентных%20водных%20условиях)] ЛИДАР**



------

<a name="singleimage"/>

### Single image

Использование одного изображения в качестве входных данных всегда сложно. Оно может быть рассмотрено уже отдельно от самого исследования

**[[:scroll:](https://abhishekkar.info/categoryshapes.pdf)] (2015) Category-Specific Object Reconstruction from a Single Image**

**[[:scroll:](https://arxiv.org/pdf/1804.05469.pdf)] (2018) Im2Struct: Recovering 3D Shape Structure from a Single RGB Image**

**[[:scroll:](https://arxiv.org/pdf/1809.03770.pdf)] (2018) 3D Human Body Reconstruction from a Single Image via Volumetric Regression**

**[[:computer:](https://cs.stanford.edu/~kaichun/impartass/)] Learning 3D Part Assembly from a Single Image** 

​	↳ **[[:space_invader:/Python](https://github.com/AntheaLi/3DPartAssembly)] Learning 3D Part Assembly from a Single Image**

​	↳ **[[:scroll:](https://arxiv.org/pdf/2003.09754.pdf)] (2020) Learning 3D Part Assembly from a Single Image**



------

<a name="pointclouds"/>

### Point Clouds

Одно из основных трехмерных представлении.

**[[:scroll:](https://arxiv.org/pdf/2001.06280v1.pdf)] (2020) Review: deep learning on 3D point clouds**

 **[[:computer:](https://www.ifp.uni-stuttgart.de/en/research/remote_sensing/als_point_cloud_classification/)] ALS Point Cloud Classification with Convolutional Neural Networks**

​	↳ **[[:scroll:](https://www.dgpf.de/src/tagung/jt2019/proceedings/proceedings/papers/23_3LT2019_Schmohl_Soergel.pdf)] (2019) ALS Klassifizierung mit Submanifold Sparse Convolutional Networks**





------

<a name="machinelearning"/>

### Machine learning

Основные модели машинного обучения в трехмерном пространстве

**[[:computer:](http://3dshapenets.cs.princeton.edu/)] 3D ShapeNets: A Deep Representation for Volumetric Shapes** 

​	↳ **[[:scroll:](http://3dshapenets.cs.princeton.edu/paper.pdf)] :ballot_box_with_check: (2015) 3D ShapeNets: A Deep Representation for Volumetric Shapes [[:heavy_division_sign:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/formulations.md#form1)] [[:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/papers/3D_ShapeNets.md)]**

**[[:computer:](https://pratulsrinivasan.github.io/nerv/)] NeRV: Neural Reflectance and Visibility Fields for Relighting and View Synthesis** 

​	↳ **[[:scroll:](https://arxiv.org/pdf/2012.03927.pdf)] (2020) NeRV: Neural Reflectance and Visibility Fields for Relighting and View Synthesis [[:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/papers/NeRV.md)]**

**[[:computer:](https://liruihui.github.io/publication/SP-GAN/)] SP-GAN: Sphere-Guided 3D Shape Generation and Manipulation** 

​	↳ **[[:space_invader:/Python/Cuda](https://github.com/liruihui/SP-GAN)] SP-GAN: Sphere-Guided 3D Shape Generation and Manipulation (SIGGRAPH 2021)**

​	↳ **[[:scroll:](https://arxiv.org/pdf/2108.04476.pdf)] (2021) SP-GAN: Sphere-Guided 3D Shape Generation and Manipulation [[:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/papers/SP_GAN_Sphere_Guided_3D_Shape_Generation_and_Manipulation.md)]**

**[[:space_invader:/Jupiter/Python](https://github.com/bmild/nerf)] NeRF: Neural Radiance Fields**





------

<a name="texture"/>

### Texture

С текстурами я пока не работаю.

**[[:scroll:](https://arxiv.org/pdf/1905.07259.pdf)] (2019) Texture Fields: Learning Texture Representations in Function Space**





------

<a name="real"/>

### Real-time 3D reconstruction

Изучаю что люди делают при реал тайм реконструкции.

**[[:computer:](https://reality.cs.ucl.ac.uk/projects/kinect/keller13realtime.html)] REAL-TIME 3D RECONSTRUCTION IN DYNAMIC SCENES USING POINT-BASED FUSION** 

​	↳ **[[:scroll:](https://reality.cs.ucl.ac.uk/projects/kinect/keller13realtime.pdf)] (2013) Real-time 3D Reconstruction in Dynamic Scenes using Point-based Fusion**

​	↳ **[[:clapper:](https://www.youtube.com/watch?v=7q-NGpuSQYg)] (JUL2013) 3DV 2013 - Real-time 3D Reconstruction in Dynamic Scenes using Point-based Fusion**

**[[:scroll:](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/kinectfusion-uist-comp.pdf)] (OCT2011) KinectFusion: Real-time 3D Reconstruction and Interaction Using a Moving Depth Camera**

**[[:scroll:](http://www.cvlibs.net/publications/Geiger2011IV.pdf)] (2011) StereoScan: Dense 3d Reconstruction in Real-time**

**[[:scroll:](https://www.sciencedirect.com/science/article/pii/S2352340921007575?via%3Dihub)] (OCT2021) DenseMatch: a dataset for real-time 3D reconstruction**

​	↳ **[[:space_invader:/Python](https://github.com/lombardm/DenseMatch_dataset/tree/v1.0.0)] 3DenseMatch_dataset**



------



<a name="driving"/>

### Autonomous Driving

Автономное вождение чаще всего попадается на глаза, так как тема ну оочень крутая :)

**[[:scroll:](https://arxiv.org/pdf/1906.05113.pdf)] (2020) A Survey of Autonomous Driving: Common Practices and Emerging Technologies**

**[[:scroll:](https://arxiv.org/pdf/1910.07738.pdf)] (MAR2020) A Survey of Deep Learning Techniques for Autonomous Driving**

**[[:clapper:](https://www.youtube.com/watch?v=6r7vDhPXmiM)] (APR2020) Zoox: ~1-Hour Fully Autonomous Drive in San Francisco with Commentary**

**[[:clapper:](https://www.reddit.com/r/interestingasfuck/comments/ewoqhc/some_of_what_goes_on_behind_teslas_auto_pilot/)] (OCT2020) Some of what goes on behind Tesla's auto pilot software**



------

<a name="others" />

## Others

Прочие ссылки, полезная информация, платформы и идеи



------

<a name="idea"/>

### Interesting idea

Собирательный контент, без определенного направления. Контент в виде статей, видео и новостных порталов. Тут я лишь собираю интересные идеи.

**[[:scroll:](https://sci-hub.se/10.1145/3150165.3150166)] (2017) Cloud-based collaborative 3D reconstruction using smartphones** 

**[[:clapper:](https://www.youtube.com/watch?app=desktop&v=kxtQqYLRaSQ)] (JUL2009) Coliseum Dubrovnik**

**[[:clapper:](https://www.youtube.com/watch?v=bTp1DRfULII)] (MAY2015) Football Stadium 3D Evacuation Simulation**

**[[:clapper:](https://www.youtube.com/watch?v=dR5G5SNI5T4)] (MAY2015) Oasys Software - MassMotion, The World's Most Advanced Crowd Simulation Software**

**[[:clapper:](https://www.youtube.com/watch?v=9SVC7XBhBpk)] (APR2017) Implicit Crowd Simulation**

**[[:clapper:](https://www.youtube.com/watch?v=y9SMd9NwoC0)] (MAR2020) Crowd simulation in Unity3D DOTS. Density & Instance colors**

**[[:scroll:](https://www.researchgate.net/publication/339447464_Unmanned_Aerial_Vehicle_Path_Planning_for_Exploration_Mapping)] (FEB2020) Unmanned Aerial Vehicle Path Planning for Exploration Mapping**

​	↳ **[[:clapper:](https://www.youtube.com/watch?v=o1RbLLVwFTA&feature=emb_title)] (MAR2020) Unmanned Aerial Vehicle Path Planning for Exploration Mapping**

**[[:computer:](https://machinelearningmastery.com/a-gentle-introduction-to-pix2pix-generative-adversarial-network/)] A Gentle Introduction to Pix2Pix Generative Adversarial Network (GAN)**

**[[:computer:](https://www.scientificamerican.com/article/how-3-d-scanning-is-reinventing-paleoanthropology/)] How 3-D Scanning Is Reinventing Paleoanthropology**

**[[:computer:](https://www.nature.com/articles/s41467-021-21326-w)] Unlocking history through automated virtual unfolding of sealed documents imaged by X-ray microtomography**

**[[:computer:](https://www.scientificamerican.com/article/a-blank-wall-can-show-how-many-people-are-in-a-room-and-what-theyre-doing/)] A Blank Wall Can Show How Many People Are in a Room and What They’re Doing**

**[[:computer:](https://www.washingtonpost.com/arts-entertainment/interactive/2021/tenement-museum/)] Take a look inside to see how the Tenement Museum has preserved its history**

**[[:computer:](https://lambdalabs.com/service/gpu-cloud?utm_source=two-minute-papers&utm_campaign=relevant-videos&utm_medium=video)] Lambda GPU Cloud for Deep Learning**

​	↳ **[[:computer:](https://nvlabs.github.io/instant-ngp/)] Instant Neural Graphics Primitives with a Multiresolution Hash Encoding**

​	↳ **[[:space_invader:](https://github.com/NVlabs/instant-ngp)] Instant Neural Graphics Primitives**

​	↳ **[[:scroll:](https://nvlabs.github.io/instant-ngp/assets/mueller2022instant.pdf)] Instant Neural Graphics Primitives with a Multiresolution Hash Encoding**

​	↳ **[[:clapper:](https://www.youtube.com/watch?v=j8tMk-GE8hY)] NVIDIA’s New AI: Wow, Instant Neural Graphics!**




------



<a name="device" />

### Devices

Интересное оборудование, камеры и прочее

**[[:busts_in_silhouette:](https://habr.com/ru/post/458458/)] Камеры глубины — тихая революция (когда роботы будут видеть) Часть 2**

**[[:clapper:](https://www.youtube.com/watch?v=3Wq3vU6Ea6A)] (FEB2017) 3D printed 3D Scanner ... in action**

**[[:clapper:](https://www.youtube.com/watch?v=xEwKarW1ZF4)] (MAY2018) F8: How A.I. and Point Cloud Reconstruction Will Make VR Realistic**

**[[:clapper:](https://www.youtube.com/watch?v=CBpZtnu1Mig)] (JUN2018) DIY 3D Scanner - Fully 3d printed photogrammetry rig**

**[[:computer:](https://www.k-lens-one.com/en/home)] K|Lens One Capture RGB + Depth with YOUR camera!**




------



<a name="platform" />

### Platforms

Полноценные платформы или проекты, работающие с реальными пользователями

**[PyTorch](https://pytorch.org)** 

​	↳ **[[:clapper:](https://www.youtube.com/watch?v=eCDBA_SbxCE)] (JUL2020) 3D Deep Learning with PyTorch3D by Nikhila Ravi**

**[Itseez3D](https://itseez3d.com)**

**[Artec3D](https://www.artec3d.com/ru)**

**[Biganto](https://biganto.com/?lang=ru)**

**[Agisoft Metashape](https://www.agisoft.com/) [[:paperclip:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/experiments/Agisoft_Metashape.md)]**

**[KazAeroSpace](https://kazaerospace.com/ru/archives/category/cartography)**

**[OPEN SOURCE VISION FOUNDATION](http://osvf.org)**

1. OpenCV - Open Source Computer Vision code plus optimized deep learning

2. Open3D - Open 3D point cloud library code

3. CARLA - Open autonomous driving simulator

4. DLG - The Deep Learning Group

**[VIVE SRWorks SDK Guide](https://hub.vive.com/storage/srworks/index.html)**

**[Visual Analysis and Perception lab](https://vap.aau.dk/about/)**

**[Forensic Architecture](https://forensic-architecture.org)**

​	↳ **[[:space_invader:/notes](https://github.com/forensic-architecture/models)] 3d models and other assets for investigations.**

​	↳ **[[:clapper:](https://www.youtube.com/watch?v=-mQ60wNgKrQ&feature=youtu.be)] :ballot_box_with_check: (NOV2020) The Beirut Port Explosions (English)**

**[PolyCam](https://poly.cam) [[:paperclip:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/experiments/PolyCam.md)]**

https://github.com/alicevision/Meshroom

------



<a name="lib" />

### Libraries

Новинки библиотек, которые можно будет применить в исследованиях, + стандартные библиотеки

**Open3D: A Modern Library for 3D Data Processing: [[:computer:](http://www.open3d.org)], [[:space_invader:/C++/Python](https://github.com/isl-org/Open3D)], [[:scroll:](http://www.open3d.org/wordpress/wp-content/paper.pdf)], [[doc](http://www.open3d.org/docs/release/) [:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/docs/Open3D_A_Modern_Library_for_3D_Data_Processing.md) [:paperclip:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/experiments/Open3D.md)], [[blog](http://www.open3d.org/blog/)]**

**Open3D-ML: [[:space_invader:/Python](https://github.com/isl-org/Open3D-ML)]** - is an extension of Open3D for 3D machine learning tasks

**OpenVINO: [[:computer:](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)], [[doc](https://docs.openvino.ai/latest/notebooks/notebooks.html)]**





------

<a name="channel" />

### Youtube channels

Крутые каналы на ютуб с аналогичным контентом

**[Two Minute Papers](https://www.youtube.com/channel/UCbfYPyITQ-7l4upoX8nvctg)**






------

<a name="author" />

### Authors

Интересные авторы, которые заинтересовали своей биографией

**Hamid Laga [[1](https://paperswithcode.com/author/hamid-laga)], [[2](https://dblp.org/pid/23/491.html)]**





------

<a name="stackoveflow" />

### Stackoveflow

Вопросы в тему, как говорится.

**[[1](https://stackoverflow.com/questions/7705377/3d-reconstruction-how-to-create-3d-model-from-2d-image)]:** 3D reconstruction -- How to create 3D model from 2D image?

**[[2](https://stackoverflow.com/questions/34280345/rgb-d-pose-estimation-with-opencv-and-python)]:** RGB-D pose estimation with OpenCv and python

https://www.reddit.com/r/computervision/comments/yiruix/what_are_open_problems_in_3d_reconstruction_sfm/







------

<a name="news" />

### Qualified search sites

Более узконаправленные сайты, для поиска нужной информации по категориям

**[[PythonRepo](https://pythonrepo.com/tag/rgbd-camera)] - Python rgbd-camera Libraries**





------

<a name="review"/>

### Under consideration

Пока не разобрала категорию, в процессе анализа.

**[[:scroll:](https://arxiv.org/pdf/1812.03828.pdf)] (2019) Occupancy Networks: Learning 3D Reconstruction in Function Space** 

​	↳ **[[:scroll:](http://www.cvlibs.net/publications/Niemeyer2019ICCV.pdf)] (2019) Occupancy Flow: 4D Reconstruction by Learning Particle Dynamics**

​	↳ **[[:clapper:](https://youtu.be/9r9TDr2Aq5A)] :ballot_box_with_check: (JUN2020) Learning 3D Reconstruction in Function Space (Long Version) [[:thought_balloon:](https://github.com/aktumar/3D_reconstruction/blob/main/additional_info/notes/youtube/Learning_3D_Rec_in_Function_Space.md)]**

​	↳ **[[слайд](http://www.cvlibs.net/talks/talk_cvpr_2020_implicit_long.pdf)] Learning 3D Reconstruction in Function Space**

**[[:space_invader:/Lua](https://github.com/Amir-Arsalan/Synthesize3DviaDepthOrSil)] Synthesizing 3D Shapes via Modeling Multi-View Depth Maps and Silhouettes with Deep Generative Networks**

​	↳ **[[:scroll:](https://openaccess.thecvf.com/content_cvpr_2017/papers/Soltani_Synthesizing_3D_Shapes_CVPR_2017_paper.pdf)] (2017) Synthesizing 3D Shapes via Modeling Multi-View Depth Maps and Silhouettes with Deep Generative Networks**

**[[:scroll:](https://arxiv.org/pdf/1901.05103.pdf)] (2019) DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation**

**[[:scroll:](https://arxiv.org/pdf/1812.02822.pdf)] (2019) Learning Implicit Fields for Generative Shape Modeling.**

**[[:scroll:](https://arxiv.org/pdf/2004.00452.pdf)] (2020) PIFuHD: Multi-Level Pixel-Aligned Implicit Function for High-Resolution 3D Human Digitization**

 **[[:computer:](https://augmentedperception.github.io/deepviewvideo/)] IMMERSIVE LIGHT FIELD VIDEO WITH A LAYERED MESH REPRESENTATION**

​	↳ **[[:scroll:](https://storage.googleapis.com/immersive-lf-video-siggraph2020/ImmersiveLightFieldVideoWithALayeredMeshRepresentation.pdf)] (2020) Immersive Light Field Video with a Layered Mesh Representation**

**[[:space_invader:/Python](https://github.com/alextrevithick/GRF)] GRF: Learning a General Radiance Field for 3D Representation and Rendering**

​	↳ **[[:scroll:](https://arxiv.org/pdf/2010.04595.pdf)] (2020) GRF: LEARNING A GENERAL RADIANCE FIELD FOR 3D SCENE REPRESENTATION AND RENDERING**

**[[:scroll:](https://arxiv.org/pdf/1912.07372.pdf)] (2020) Differentiable Volumetric Rendering: Learning Implicit 3D Representations without .3D Supervision**

**[[:computer:](https://www.matthewtancik.com/learnit)] Learned Initializations for Optimizing Coordinate-Based Neural Representations**

​	↳ **[[:space_invader:/Python](https://github.com/sanowar-raihan/nerf-meta)] NeRF Meta Learning With PyTorch**

​	↳ **[[:space_invader:/Jupiter](https://github.com/tancik/learnit)] Learned Initializations for Optimizing Coordinate-Based Neural Representations**

​	↳ **[[:space_invader:/Jupiter/Python](https://github.com/kwea123/nerf_pl)] NeRF (Neural Radiance Fields) and NeRF in the Wild using pytorch-lightning**

ᅠ	↳ **[[:clapper:](https://www.youtube.com/watch?v=TQj-KUQophI&list=PLDV2CyUo4q-K02pNEyDr7DYpTQuka3mbV&index=2)] (MAY2020) NeRF (Neural Radiance Fields) tutorial using google colab part1**

​	↳ **[[:scroll:](https://arxiv.org/pdf/2012.02189.pdf)] (2021) Learned Initializations for Optimizing Coordinate-Based Neural Representations**

**[[:computer:](http://marrnet.csail.mit.edu)] MarrNet: 3D Shape Reconstruction via 2.5D Sketches**

​	↳ **[[:scroll:](http://marrnet.csail.mit.edu/papers/marrnet_nips.pdf)] (2017) MarrNet: 3D Shape Reconstruction via 2.5D Sketches**

​	↳ **[[:scroll:](http://3dinterpreter.csail.mit.edu/papers/3dinn_ijcv.pdf)] (APR2018) 3D Interpreter Networks for Viewer-Centered Wireframe Modeling**

​	↳ **[[:scroll:](http://3dgan.csail.mit.edu/papers/3dgan_nips.pdf)] (2016) Learning a Probabilistic Latent Space of Object Shapes via 3D Generative-Adversarial Modeling**https://3dphoto.io/uploader/# 3D reconstruction

https://towardsdatascience.com/3d-point-cloud-clustering-tutorial-with-k-means-and-python-c870089f3af8

https://www.cs.cornell.edu/~asaxena/learningdepth/ijcv_monocular3dreconstruction.pdf

https://api-2d3d-cad.com/3d_reconstruction_android/#2

​	↳ **[[:scroll:](http://shapehd.csail.mit.edu/papers/shapehd_eccv.pdf)] (2018) Learning Shape Priors for Single-View 3D Completion and Reconstruction**

​	↳ **[[:scroll:](http://genre.csail.mit.edu/papers/genre_nips.pdf)] (2018) Learning to Reconstruct Shapes from Unseen Classes**

**[[:space_invader:/Jupiter/Python](https://github.com/normandipalo/faceID_beta/blob/master/faceid_beta.ipynb)] faceID_beta**

**[[:scroll:](https://arxiv.org/pdf/2204.13359v2.pdf)] (MAY2022) POLY-CAM: HIGH RESOLUTION CLASS ACTIVATION MAP FOR CONVOLUTIONAL NEURAL NETWORKS**

​	↳ **[[:space_invader:/Python](https://github.com/aenglebert/polycam)] Polycam**

[https://3dphoto.io/uploader/# 3D reconstruction]()

[https://towardsdatascience.com/3d-point-cloud-clustering-tutorial-with-k-means-and-python-c870089f3af8]()

[https://www.cs.cornell.edu/~asaxena/learningdepth/ijcv_monocular3dreconstruction.pdf]()

[https://api-2d3d-cad.com/3d_reconstruction_android/#2]()

[https://www.diva-portal.org/smash/get/diva2:689500/FULLTEXT01.pdf]()

[https://www.mdpi.com/1424-8220/22/7/2469]()
