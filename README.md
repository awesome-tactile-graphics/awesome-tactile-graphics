<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Living Repository for Generative AI for Tactile Accessibility.
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/your-org/generative-tactile-ai/pulls)
[![CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](LICENSES/LICENSE-CC-BY-4.0)
[![MIT License](https://img.shields.io/badge/code-MIT-orange.svg)](LICENSES/LICENSE-MIT)
![Last Updated](https://img.shields.io/badge/last%20updated-November%202025-lightgrey.svg)

This repository accompanies the paper  
> **Generative AI for Tactile Accessibility: A Systematic Literature Review of Emerging Methods and Gaps**  [under review]

*Authors: Adnan Khan, Abbas Akkasi, Darya Taratynova, Majid Komeili*  

It serves as a **living resource** that tracks research, datasets, and tools at the intersection of **Generative AI** and **tactile accessibility for blind and low-vision (BLV)** users.



## Scope

This repository curates **generative approaches** that are *tactile-relevant*:

- Methods using **GANs**, **Diffusion Models**, or **Multimodal LLMs/MLLMs**
- Direct tactile outputs: embossable linework, textures, or vibrotactile signals  
- Generative steps in tactile workflows (e.g., contour simplification, image→tactile translation)  

**Out of scope:**  
Purely rule-based methods, hardware-only systems, or visual-only tasks.
## Contribute

Add new papers, tools, or resources by opening a Pull Request.  

👉 See [`CONTRIBUTING.md`](CONTRIBUTING.md) for:
- Contribution workflow  
- CSV schema for the papers table  
- Tag definitions and naming standards  


## Selected papers
<!-- SELECTED_PAPERS:START -->

| Year | Title & Links | Authors | Venue | Type | Tags | Notes |
|:----:|:--------------|:--------|:------|:-----|:-----|:------|
| 2025 | [A Comparative Evaluation of GenAI-Assisted Tactile Graphics from the Perspective of Totally Blind Professionals in Tactile Graphic Supervision](https://doi.org/10.1145/3663547.3759740)<br/>[DOI](https://doi.org/10.1145/3663547.3759740) · [PDF](https://dl.acm.org/doi/10.1145/3663547.3759740) | Kengo Tanaka; Ayaka Tsutsui; Yoichi Ochiai | ASSETS '25: The 27th International ACM SIGACCESS Conference on Computers and Accessibility | conference | gan; tactile-graphic; user-study; blv-eval | Evaluates GenAI-assisted tactile graphics for picture books; highlights human-in-loop refinement. |
| 2025 | [AI-generated tactile graphics for visually impaired children: A usability study of a multimodal educational product](https://doi.org/10.1016/j.ijhcs.2025.103525)<br/>[DOI](https://doi.org/10.1016/j.ijhcs.2025.103525) · [PDF](https://www.sciencedirect.com/science/article/pii/S1071581925000825) | Wu, Hantian; Yang, Hongyi; Chang, Fangyuan; Zhu, Dian; Liu, Zhao | International Journal of Human-Computer Studies | journal | diffusion; tactile-graphic; accessibility-tool; education; user-study | Multimodal LLM and DALL·E-based tool generating tactile graphics and audio for blind children; evaluated with 19 users. |
| 2025 | [TactileNet: Bridging the Accessibility Gap with AI-Generated Tactile Graphics for Individuals with Vision Impairment](https://arxiv.org/abs/2504.04722)<br/>[arXiv](https://arxiv.org/abs/2504.04722) · [PDF](https://arxiv.org/pdf/2504.04722.pdf) | Khan, Adnan; Choubineh, Alireza; Shaaban, Mai A.; Akkasi, Abbas; Komeili, Majid | arXiv | preprint | diffusion; tactile-graphic; accessibility-tool; dataset; prototype | Stable Diffusion–based framework using LoRA and DreamBooth to generate embossing-ready tactile graphics with high structural fidelity. |
| 2025 | [TexSenseGAN: A User-Guided System for Optimizing Texture-Related Vibrotactile Feedback Using GAN](https://arxiv.org/abs/2407.11467)<br/>[arXiv](https://arxiv.org/abs/2407.11467) · [PDF](https://arxiv.org/pdf/2407.11467.pdf) | Zhang, Mingxin; Terui, Shun; Makino, Yasutoshi; Shinoda, Hiroyuki | IEEE Transactions on Haptics | journal | gan; vibrotactile; user-study | User-guided GAN for optimizing texture-related vibrotactile feedback; no BLV-specific validation reported. |
| 2025 | [Text-Guided Image-to-Image Translation for Converting RGB Maps to Tactile Images](https://doi.org/10.22215/etd/2025-16415)<br/>[DOI](https://doi.org/10.22215/etd/2025-16415) · [PDF](https://carleton.scholaris.ca/items/028aa7a2-8080-4a53-ba5f-bbd543d4f170) | Choubineh, Alireza | Carleton University (PhD Thesis) | thesis | diffusion; tactile-map; translation; dataset | Text-guided image-to-image translation generates tactile maps from RGB inputs; builds dataset of 9.8k triplets. |
| 2024 | [A Step Towards Automated and Generalizable Tactile Map Generation Using Generative Adversarial Networks](https://arxiv.org/abs/2412.07191)<br/>[arXiv](https://arxiv.org/abs/2412.07191) · [PDF](https://arxiv.org/pdf/2412.07191) | Hobson, David G.; Komeili, Majid | arXiv | preprint | gan; tactile-map; dataset; accessibility-tool | Introduces tactile map dataset of 6.5k Google Maps samples and GANs for automatic map element extraction and inpainting. |
| 2024 | [AltCanvas: A Tile-Based Image Editor with Generative AI for Blind or Visually Impaired People](https://doi.org/10.1145/3663548.3675600)<br/>[DOI](https://doi.org/10.1145/3663548.3675600) · [PDF](https://dl.acm.org/doi/pdf/10.1145/3663548.3675600) | Lee, Seonghee; Kohga, Maho; Landau, Steve; O'Modhrain, Sile; Subramonyam, Hari | ACM ASSETS 2024: The 26th International ACM SIGACCESS Conference on Computers and Accessibility | conference | diffusion; tactile-graphic; accessibility-tool; blv-eval; user-study | Tile-based editor allowing blind users to create and edit visual scenes via generative AI with audio feedback. |
| 2024 | [Artificial Intelligence-Driven Text-to-Tactile Graphics Generation for Visual Impaired People](https://ceur-ws.org/Vol-3777/short4.pdf)<br/>[PDF](https://ceur-ws.org/Vol-3777/short4.pdf) | Dzhurynskyi, Yehor; Mayik, Volodymyr; Mayik, Lyudmyla | ProfIT AI 2024 (Proceedings) | conference | transformer; tactile-graphic; accessibility-tool; education | Transformer-based text-to-tactile synthesis for educational accessibility. |
| 2023 | [Text to haptics: method and case studies of designing tactile graphics for inclusive tactile picture books by digital fabrication and generative AI](https://doi.org/10.1145/3588029.3595471)<br/>[DOI](https://doi.org/10.1145/3588029.3595471) · [PDF](https://dl.acm.org/doi/10.1145/3588029.3595471) | Tanaka, Kengo; Fushimi, Tatsuki; Tsutsui, Ayaka; Ochiai, Yoichi | ACM SIGGRAPH 2023 Labs | conference | diffusion; tactile-graphic; accessibility-standard; education | Diffusion-based tactile picture book overlays integrating generative AI and 3D printing. |
| 2021 | [Visual-Tactile Cross-Modal Data Generation Using Residue-Fusion GAN with Feature-Matching and Perceptual Losses](https://doi.org/10.1109/LRA.2021.3095925)<br/>[DOI](https://doi.org/10.1109/LRA.2021.3095925) · [arXiv](https://arxiv.org/abs/2107.05468) · [PDF](https://ieeexplore.ieee.org/document/9479777/) | Cai, Shaoyu; Zhu, Kening; Ban, Yuki; Narumi, Takuji | IEEE Robotics and Automation Letters | journal | gan; vibrotactile; texture-generation; user-study | GAN-based cross-modal synthesis between visual textures and vibrotactile feedback. |
| 2019 | [Generating Vibrotactile Patterns from Texture Images Using Conditional GANs](https://doi.org/10.1007/978-3-319-93399-3_3)<br/>[DOI](https://doi.org/10.1007/978-3-319-93399-3_3) · [arXiv](https://arxiv.org/abs/1902.07480) · [PDF](https://link.springer.com/chapter/10.1007/978-3-319-93399-3_3) | Ujitoko, Yuki; Ban, Yoshinori | International Conference on Human Haptic Sensing and Touch Enabled Computer Applications (EuroHaptics) | conference | gan; vibrotactile; user-study | Early conditional GAN generating vibrotactile signals from texture images or attributes. |
<!-- SELECTED_PAPERS:END -->
### 📁 Additional Resources

A growing collection of curated materials is available in the **`resources/`** directory of this repository. These files provide practical support for researchers, educators, and designers working on tactile accessibility:

- **books.md** — Key textbooks and reference books on tactile design, accessibility, and non-visual information presentation.  
- **datasets.md** — Public datasets relevant to tactile graphics, BLV accessibility, and image–to–tactile translation.  
- **guides.md** — Practical guides, standards summaries, and how-to documents for creating high-quality tactile graphics.  
- **tools.md** — A list of software tools, libraries, and workflows for generating, editing, and evaluating tactile images.

You can access them here:  
https://github.com/awesome-tactile-graphics/awesome-tactile-graphics/tree/main/resources


## License

This project uses a **dual-license structure**:

- **Content** (paper, docs, CSVs, figures): [CC BY 4.0](LICENSES/LICENSE-CC-BY-4.0)  
- **Code** (scripts, notebooks): [MIT](LICENSES/LICENSE-MIT)

By submitting a pull request, you agree to license your contribution accordingly and include an SPDX header when applicable.

## How to Cite

If you use this repository, please cite:

> **Generative AI for Tactile Accessibility: A Systematic Literature Review of Emerging Methods and Gaps**  
> *Authors: Adnan Khan, Abbas Akkasi, Darya Taratynova, Majid Komeili*  
> *GitHub Repository: https://github.com/awesome-tactile-graphics/awesome-tactile-graphics*  
> *DOI: coming soon*  

### Acknowledgements

We extend our sincere thanks to the volunteers from the **Intelligent Machines Lab (iML) at Carleton University** for generously contributing their time, insights, and effort to this project.

