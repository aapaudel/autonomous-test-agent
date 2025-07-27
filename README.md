AI Test Geerator

This project buids an AI - powered test generation tool which is designed to automatically generate unit tests from Python source code. Its goal is to reduce the manual effort involved in writing and maintaining tests, especially as codebase grow and evlove.
Writing test case is tedious, error oriented and often skipped under tight deadlines. This tool aims to reduce the early generation of test cases and reduce the effort put on in generating test cases.
- Ensure better code coverage
- Adapt to code changes quickly
- Catch bugs early through automated edge-aware testing

In an especially Agime workflows the rapic code canege or a minor code change leads to the regression testing becomes a bottleneck.

Tools Used:

- Python 3.8 Core
- Pytest as a testing framework
- Starcoder Model to generate meaning ful test cases from code prompts
- Abstract Syntax Tree (AST) for parsing the files and extracting files
- Watcher Unility to track the modified files for selective test generation
- Shell Script a CLI wrapper for ease of use (generate-tests.sh)
- Tailored test generation prompts for better model results

The Thought Process

- Using an Extractor function to parse the source code using ast that identifes the functions,
each function is converted into a natural language prompt using a template and "StarCoder" model generates a corresponding test case
- Clean the test code and saved 
- Test cases are executed using pytest

- Modes of the Operation are categorized in three catogories:
    1. Generating test cases for whole source code
    2. Changes in the specific files via watchere thet looks for changes and regenerate the test case accordingly
    3. Specify the test case for specific files manually

Future work/ working on

- Add support to open AI, claude and local LLMs like Code Llama
- Value Aware Test Generation which is much syarter test with inputs
- generate the test palan with the documanetation
- GUI and non - termial user approach
- Generating tests that include mcks, file reads and database stubs

Resource for more understanding on the similar works:

Z. Gu, H. Zhang, and C. Zhang,
“TestART: Improving LLM-Based Unit Testing via Co-Evolution of Generation and Repair,”
arXiv preprint arXiv:2408.03095, Aug. 2024.
Available: https://arxiv.org/abs/2408.03095

Y. Li, D. Ye, F. Thung, and D. Lo,
“An Empirical Study of Unit Test Generation with Large Language Models,”
arXiv preprint arXiv:2406.18181, June 2024.
Available: https://arxiv.org/abs/2406.18181

Y. Zhang, L. Li, and M. Zhou,
“APT: Property-Based Retrieval-Augmented Unit Test Generation,”
arXiv preprint arXiv:2410.13542, Oct. 2024.
Available: https://arxiv.org/abs/2410.13542

J. Ryan, S. Chattopadhyay, and T. Henzinger,
“SymPrompt: Coverage-Guided Test Generation for LLMs in Regression Settings,”
arXiv preprint arXiv:2403.16218, Mar. 2024.
Available: https://arxiv.org/abs/2403.16218

“Tree‑sitter: An incremental parsing system for programming tools,”
Tree‑sitter, 2024. [Online]. Available: http://tree‑sitter.github.io/tree‑sitter

Figshare Data Package, 2024. [Online]. Available: https://doi.org/10.6084/m9.figshare.25983166


Lakshya A. Agrawal, Aditya Kanade, Navin Goyal, Shuvendu K. Lahiri, and Sriram K. Rajamani. 2023. Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context. In NeurIPS.

Saranya Alagarsamy, Chakkrit Tantithamthavorn, and Aldeida Aleti. 2023.
A3Test: Assertion-Augmented Automated Test Case Generation. CoRR
abs/2302.10352 (2023).

Xavier Amatriain. 2024. Prompt Design and Engineering: Introduction and Advanced Methods. CoRR abs/2401.14423 (2024).

Shreya Bhatia, Tarushi Gandhi, Dhruv Kumar, and Pankaj Jalote. 2023. Unit
Test Generation using Generative AI : A Comparative Performance Analysis of
Autogeneration Tools. CoRR abs/2312.10622 (2023).

Mark Chen, Jerry Tworek, Heewoo Jun, , et al. 2021. Evaluating Large Language
Models Trained on Code. CoRR abs/2107.03374 (2021).

Xiangping Chen, Xing Hu, Yuan Huang, He Jiang, Weixing Ji, Yanjie Jiang,
Yanyan Jiang, Bo Liu, Hui Liu, Xiaochen Li, Xiaoli Lian, Guozhu Meng, Xin Peng,
Hailong Sun, Lin Shi, Bo Wang, Chong Wang, Jiayi Wang, Tiantian Wang, Jifeng
Xuan, Xin Xia, Yibiao Yang, Yixin Yang, Li Zhang, Yuming Zhou, and Lu Zhang.
[n. d.]. Deep Learning-based Software Engineering: Progress, Challenges, and
Opportunities. SCIENCE CHINA Information Sciences ([n. d.]), –.

Jacob Cohen. 2013. Statistical power analysis for the behavioral sciences. Routledge.

Arghavan Moradi Dakhel, Amin Nikanjam, Vahid Majdinasab, Foutse Khomh,
and Michel C. Desmarais. 2024. Effective test generation using pre-trained Large
Language Models and mutation testing. Inf. Softw. Technol. 171 (2024), 107468.

DeepSeek. 2023. DeepSeek Coder: Let the Code Write Itself.
https://github.com/deepseek-ai/DeepSeek-Coder.

Elizabeth Dinella, Gabriel Ryan, Todd Mytkowicz, and Shuvendu K Lahiri. 2022.
Toga: A neural method for test oracle generation. In Proceedings of the 44th International Conference on Software Engineering. 2130–2141.

Xueying Du, Mingwei Liu, Kaixin Wang, , et al. 2024. Evaluating Large Language
Models in Class-Level Code Generation. In ICSE. ACM, 81:1–81:13.

Eduard Paul Enoiu, Adnan Causevic, Thomas J. Ostrand, Elaine J. Weyuker,
Daniel Sundmark, and Paul Pettersson. 2016. Automated test generation using
model checking: an industrial evaluation. Int. J. Softw. Tools Technol. Transf. 18,
3 (2016), 335–353.

Angela Fan, Beliz Gokkaya, Mark Harman, Mitya Lyubarskiy, Shubho Sengupta,
Shin Yoo, and Jie M. Zhang. 2023. Large Language Models for Software Engineering: Survey and Open Problems. In ICSE-FoSE. IEEE, 31–53.

Gordon Fraser and Andrea Arcuri. 2011. EvoSuite: automatic test suite generation for object-oriented software. In SIGSOFT FSE. ACM, 416–419.

Angelo Gargantini and Constance L. Heitmeyer. 1999. Using Model Checking to
Generate Tests from Requirements Specifications. In ESEC / SIGSOFT FSE (Lecture Notes in Computer Science, Vol. 1687). Springer, 146–162.

Qi Guo, Junming Cao, Xiaofei Xie, Shangqing Liu, Xiaohong Li, Bihuan Chen,
and Xin Peng. 2024. Exploring the potential of chatgpt in automated code refinement: An empirical study. In Proceedings of the 46th IEEE/ACM International
Conference on Software Engineering. 1–13.

Stefan Hackmann, Haniyeh Mahmoudian, Mark Steadman, and Michael
Schmidt. 2024. Word Importance Explains How Prompts Affect Language Model
Outputs. CoRR abs/2403.03028 (2024).

Marc Hoffmann and Michael Ernst. 2021. JaCoCo: Java Code Coverage Library.
https://www.jacoco.org. Accessed: 2024-05-19.

Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. 2020. The Curious Case of Neural Text Degeneration. In ICLR. OpenReview.net.

Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong Wang, Li Li, Xiapu Luo,
David Lo, John C. Grundy, and Haoyu Wang. 2023. Large Language Models for
Software Engineering: A Systematic Literature Review. CoRR abs/2308.10620
(2023).

Jiajun Jiang, Ran Wang, Yingfei Xiong, Xiangping Chen, and Lu Zhang. 2019.
Combining spectrum-based fault localization and statistical debugging: An empirical study. In 2019 34th IEEE/ACM International Conference on Automated Software Engineering (ASE). IEEE, 502–514.

Jiajun Jiang, Yumeng Wang, Junjie Chen, Delin Lv, and Mengjiao Liu. 2023.
Variable-Based Fault Localization via Enhanced Decision Tree. ACM Transactions on Software Engineering and Methodology 33, 2 (2023), 1–32.

Jiajun Jiang, Yingfei Xiong, and Xin Xia. 2019. A manual inspection of defects4j
bugs and its implications for automatic program repair. Science china information
sciences 62 (2019), 1–16.

Jiajun Jiang, Yingfei Xiong, Hongyu Zhang, Qing Gao, and Xiangqun Chen.
2018. Shaping program repair space with existing patches and similar code. In Proceedings of the 27th ACM SIGSOFT International Symposium on Software Testing and Analysis (Amsterdam, Netherlands) (ISSTA
2018). Association for Computing Machinery, New York, NY, USA, 298–309.
https://doi.org/10.1145/3213846.3213871

Shengbei Jiang, Jiabao Zhang, Wei Chen, Bo Wang, Jianyi Zhou, and Jie Zhang.
2024. Evaluating Fault Localization and Program Repair Capabilities of Existing Closed-Source General-Purpose LLMs. In Proceedings of the 1st International
Workshop on Large Language Models for Code. 75–78.

René Just, Darioush Jalali, and Michael D. Ernst. 2014. Defects4J: a database of
existing faults to enable controlled testing studies for Java programs. In ISSTA.
ACM, 437–440.

Sungmin Kang, Juyeon Yoon, and Shin Yoo. 2023. Large language models are fewshot testers: Exploring llm-based general bug reproduction. In 2023 IEEE/ACM
45th International Conference on Software Engineering (ICSE). IEEE, 2312–2323.

Vladimir Karpukhin, Barlas Oguz, Sewon Min, Patrick S. H. Lewis, Ledell Wu,
Sergey Edunov, Danqi Chen, and Wen-tau Yih. 2020. Dense Passage Retrieval
for Open-Domain Question Answering. In EMNLP (1). Association for Computational Linguistics, 6769–6781.

Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney, Caiming Xiong, and
Richard Socher. 2019. CTRL: A Conditional Transformer Language Model for
Controllable Generation. CoRR abs/1909.05858 (2019).

Divya Kumar and Krishn Kumar Mishra. 2016. The impacts of test automation
on software’s cost, quality and time to market. Procedia Computer Science 79
(2016), 8–15.

Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng,
Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. 2023. Efficient memory management for large language model serving with pagedattention. In Proceedings of the 29th Symposium on Operating Systems Principles. 611–626.

Caroline Lemieux, Jeevana Priya Inala, Shuvendu K Lahiri, and Siddhartha Sen.
2023. CODAMOSA: Escaping coverage plateaus in test generation with pretrained large language models. In International conference on software engineering (ICSE).

Brian Lester, Rami Al-Rfou, and Noah Constant. 2021. The Power of Scale for
Parameter-Efficient Prompt Tuning. In EMNLP (1). Association for Computational Linguistics, 3045–3059.

Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman
Mohamed, Omer Levy, Ves Stoyanov, and Luke Zettlemoyer. 2019. Bart: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension. arXiv preprint arXiv:1910.13461 (2019).

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir
Karpukhin, Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp
tasks. Advances in Neural Information Processing Systems 33 (2020), 9459–9474.

Jia Li, Yongmin Li, Ge Li, and Zhi Jin. 2023. Structured Chain-of-Thought Prompting for Code Generation. CoRR (2023).

Kefan Li and Yuan Yuan. 2024. Large Language Models as Test Case Generators:
Performance Evaluation and Enhancement. CoRR abs/2404.13340 (2024).

Tsz-On Li, Wenxi Zong, Yibo Wang, Haoye Tian, Ying Wang, Shing-Chi Cheung,
and Jeff Kramer. 2023. Nuances are the key: Unlocking chatgpt to find failureinducing tests with differential prompting. In 2023 38th IEEE/ACM International
Conference on Automated Software Engineering (ASE). IEEE, 14–26.

Yichen Li, Yintong Huo, Zhihan Jiang, Renyi Zhong, Pinjia He, Yuxin Su, and
Michael R Lyu. 2023. Exploring the effectiveness of llms in automated logging
generation: An empirical study. arXiv preprint arXiv:2307.05950 (2023).

Zongjie Li, Chaozheng Wang, Pingchuan Ma, Chaowei Liu, Shuai Wang,
Daoyuan Wu, Cuiyun Gao, and Yang Liu. 2024. On extracting specialized code
abilities from large language models: A feasibility study. In Proceedings of the
IEEE/ACM 46th International Conference on Software Engineering. 1–13.

Jingjing Liang, Ruyi Ji, Jiajun Jiang, Shurui Zhou, Yiling Lou, Yingfei Xiong, and
Gang Huang. 2021. Interactive patch filtering as debugging aid. In 2021 IEEE
International Conference on Software Maintenance and Evolution (ICSME). IEEE,
239–250.

Fang Liu, Yang Liu, Lin Shi, Houkun Huang, Ruifeng Wang, Zhen Yang, and Li
Zhang. 2024. Exploring and Evaluating Hallucinations in LLM-Powered Code
Generation. arXiv preprint arXiv:2404.00971 (2024).

Hanmeng Liu, Zhiyang Teng, Leyang Cui, Chaoli Zhang, Qiji Zhou, and Yue
Zhang. 2023. Logicot: Logical chain-of-thought instruction-tuning data collection with gpt-4. arXiv preprint arXiv:2305.12147 (2023).

Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, and Lingming Zhang. 2023. Is
Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large
Language Models for Code Generation. arXiv preprint arXiv:2305.01210 (2023)

Kui Liu, Anil Koyuncu, Dongsun Kim, and Tegawendé F Bissyandé. 2019. Tbar:
Revisiting template-based automated program repair. In Proceedings of the 28th
ACM SIGSOFT international symposium on software testing and analysis. 31–42.

Antonio Mastropaolo, Luca Pascarella, Emanuela Guglielmi, Matteo Ciniselli, Simone Scalabrino, Rocco Oliveto, and Gabriele Bavota. 2023. On the robustness
of code generation techniques: An empirical study on github copilot. In 2023
IEEE/ACM 45th International Conference on Software Engineering (ICSE). IEEE,
2149–2160.

Facundo Molina and Alessandra Gorla. 2024. Test Oracle Automation in the era
of LLMs. arXiv preprint arXiv:2405.12766 (2024).

Daye Nam, Andrew Macvean, Vincent Hellendoorn, Bogdan Vasilescu, and Brad
Myers. 2024. Using an llm to help with code understanding. In Proceedings of
the IEEE/ACM 46th International Conference on Software Engineering. 1–13.

Changan Niu, Chuanyi Li, Vincent Ng, Dongxiao Chen, Jidong Ge, and Bin Luo.
2023. An Empirical Comparison of Pre-Trained Models of Source Code. In ICSE.
On the Evaluation of Large Language Models in Unit Test Generation ASE ’24, October 27-November 1, 2024, Sacramento, CA, USA
IEEE, 2136–2148.

Wendkûuni C. Ouédraogo, Laura Plein, Abdoul Kader Kaboré, Andrew Habib,
Jacques Klein, David Lo, and Tegawendé F. Bissyandé. 2023. Enriching Automatic Test Case Generation by Extracting Relevant Test Inputs from Bug Reports.
CoRR abs/2312.14898 (2023).

Shuyin Ouyang, Jie M. Zhang, Mark Harman, and Meng Wang. 2023. LLM is
Like a Box of Chocolates: the Non-determinism of ChatGPT in Code Generation.
CoRR abs/2308.02828 (2023).

Julie Pallant. 2020. SPSS survival manual: A step by step guide to data analysis
using IBM SPSS. Routledge.

Fabio Palomba, Dario Di Nucci, Annibale Panichella, Rocco Oliveto, and Andrea
De Lucia. 2016. On the diffusion of test smells in automatically generated test
code: An empirical study. In 2016 IEEE/ACM 9th International Workshop on
Search-Based Software Testing (SBST). IEEE, 5ś14 (2016).

Rangeet Pan, Ali Reza Ibrahimzada, Rahul Krishna, Divya Sankar, Lambert Pouguem Wassi, Michele Merler, Boris Sobolev, Raju Pavuluri, Saurabh
Sinha, and Reyhaneh Jabbarvand. 2024. Lost in translation: A study of bugs
introduced by large language models while translating code. In Proceedings of
the IEEE/ACM 46th International Conference on Software Engineering. 1–13.

Md. Rizwan Parvez, Wasi Uddin Ahmad, Saikat Chakraborty, Baishakhi Ray,
and Kai-Wei Chang. 2021. Retrieval Augmented Code Generation and Summarization. In EMNLP (Findings). Association for Computational Linguistics, 2719–
2734.

Corina S. Pasareanu, Peter C. Mehlitz, David H. Bushnell, Karen Gundy-Burlet,
Michael R. Lowry, Suzette Person, and Mark Pape. 2008. Combining unit-level
symbolic execution and system-level concrete execution for testing NASA software. In ISSTA. ACM, 15–26.

Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jérémy Rapin, Artyom
Kozhevnikov, Ivan Evtimov, Joanna Bitton, Manish Bhatt, Cristian CantonFerrer, Aaron Grattafiori, Wenhan Xiong, Alexandre Défossez, Jade Copet, Faisal
Azhar, Hugo Touvron, Louis Martin, Nicolas Usunier, Thomas Scialom, and
Gabriel Synnaeve. 2023. Code Llama: Open Foundation Models for Code. CoRR
abs/2308.12950 (2023).

Pranab Sahoo, Ayush Kumar Singh, Sriparna Saha, Vinija Jain, Samrat Mondal,
and Aman Chadha. 2024. A Systematic Survey of Prompt Engineering in Large
Language Models: Techniques and Applications. arXiv preprint arXiv:2402.07927
(2024).

Max Schäfer, Sarah Nadi, Aryaz Eghbali, and Frank Tip. 2024. An Empirical
Evaluation of Using Large Language Models for Automated Unit Test Generation. IEEE Trans. Software Eng. 50, 1 (2024), 85–105.

Domenico Serra, Giovanni Grano, Fabio Palomba, Filomena Ferrucci, Harald C
Gall, and Alberto Bacchelli. 2019. On the effectiveness of manual and automatic
unit test generation: ten years later. In 2019 IEEE/ACM 16th International Conference on Mining Software Repositories (MSR). IEEE, 121–125.

Mohammed Latif Siddiq, Simantika Dristi, Joy Saha, and Joanna Santos. 2024.
Quality Assessment of Prompts Used in Code Generation. arXiv preprint
arXiv:2404.10155 (2024).

Mohammed Latif Siddiq, Joanna C. S. Santos, Ridwanul Hasan Tanvir, Noshin Ulfat, Fahmid Al Rifat, and Vinicius Carvalho Lopes. 2023. Exploring the Effectiveness of Large Language Models in Generating Unit Tests. CoRR abs/2305.00418
(2023).

André Silva, Nuno Saavedra, and Martin Monperrus. 2024. GitBug-Java: A Reproducible Benchmark of Recent Java Bugs. CoRR abs/2402.02961 (2024).

Weisong Sun, Chunrong Fang, Yudu You, Yun Miao, Yi Liu, Yuekang Li, Gelei
Deng, Shenghan Huang, Yuchen Chen, Quanjun Zhang, Hanwei Qian, Yang Liu,
and Zhenyu Chen. 2023. Automatic Code Summarization via ChatGPT: How
Far Are We? CoRR abs/2305.12865 (2023).

Weifeng Sun, Hongyan Li, Meng Yan, Yan Lei, and Hongyu Zhang. 2023. Revisiting and Improving Retrieval-Augmented Deep Assertion Generation. In ASE.
IEEE, 1123–1135.

Yutian Tang, Zhijie Liu, Zhichao Zhou, and Xiapu Luo. 2023. ChatGPT vs SBST:
A Comparative Assessment of Unit Test Suite Generation. CoRR abs/2307.00588
(2023).

Hugo Touvron, Louis Martin, Kevin Stone, et al. 2023. Llama 2: Open Foundation
and Fine-Tuned Chat Models. CoRR abs/2307.09288 (2023).

Michele Tufano, Dawn Drain, Alexey Svyatkovskiy, Shao Kun Deng, and Neel
Sundaresan. 2020. Unit Test Case Generation with Transformers. CoRR
abs/2009.05617 (2020).

Jeffrey M. Voas. 1992. PIE: A Dynamic Failure-Based Technique. IEEE Trans.
Software Eng. 18, 8 (1992), 717–727.
