<!-- ---
logo: assets/images/uottawa_hor_wg9.png
--- -->


<head>
    <script async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

      



## Introduction
[Introduction of this project.XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX.]  
[Introduction of this project.XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX.]


[Introduction of this project.XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX.]  
[Introduction of this project.XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX XXX.]  


## Model 1
Introduction of model XXXXXXX.

You can add a link: [link to model 1]()


Mathematical formula:

$$
x_1 + y^2
$$

Display as inline: $x_1 + y^2$

Table:

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

Image:  
{:refdef: style="text-align: center;"}
![image demo](images/image_demo.png){:height="50%" width="80%"}
{: refdef}

Code block:
```python
import torch
import torch.nn as nn


class CRF(nn.Module):
    """Conditional random field.

    This module implements a conditional random field. The forward computation
    of this class computes ...
    
    Args:
        num_tags: Number of tags.
        batch_first: Whether the first dimension corresponds to the size of a minibatch.
    
    Attributes:
        start_transitions (`~torch.nn.Parameter`): Start transition score tensor of size
            ``(num_tags,)``.
    """
    
    def __init__(self, num_tags, batch_first=True):
        if num_tags <= 0:
            raise ValueError(f'invalid number of tags: {num_tags}')
        super(CRF, self).__init__()
        self.num_tags = num_tags
```

## Model 2
Introduction of model XXXXXXX.

[link to model 2]()

## ...