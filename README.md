# Dynamic-Scene-Reconstruction-with-Physics-Informed-3D-Gaussians
High-Fidelity Dynamic Scene Reconstruction with Physics-Informed 3D Gaussians: Bridging Real-time Rendering and Physical Consistency
## Dataset

In our paper, we use:

- synthetic dataset from [D-NeRF](https://www.albertpumarola.com/research/D-NeRF/index.html).

## Run

### Environment

```shell
conda create -n physics_gaussian_env python=3.7
conda activate physics_gaussian_env

# install pytorch
pip install torch==1.13.1+cu116 torchvision==0.14.1+cu116 --extra-index-url https://download.pytorch.org/whl/cu116

# install dependencies
pip install -r requirements.txt
```
### Train

**D-NeRF:**

```shell
python train.py -s path/to/your/d-nerf/dataset -m output/exp-name --eval --is_blender
```
### Render & Evaluation

```shell
python render.py -m output/exp-name --mode render
python metrics.py -m output/exp-name
```

