# Hate Speech Classification

# Problem Statement:
The rapid evolution of AI has ushered in a host of challenges, including bias, privacy, and security concerns. We’ve observed instances where users have requested sensitive information from consumer chatbot applications. It’s imperative to implement measures that prevent the leakage of harmful or sensitive information to the public. Given that large language models (LLMs) powering these chatbot applications are trained on vast amounts of data from diverse sources, there’s a risk that they might encounter or generate hate speech or critical information. Therefore, it’s crucial to have safeguards in place to classify whether a user’s prompt could lead to the generation of hate speech.

# Solution:
While an LLM could potentially solve this problem, the high deployment costs for such a simple task of identifying hate or harmful language make it less feasible. Hence, this project focuses on a simpler, more cost-effective solution. We propose a compact LSTM network that is not only easy to implement but also significantly reduces the compute budget while effectively solving the problem.

# Applications include:
1. **Social Media Moderation:** filter out hate speech in comments, posts, and private messages on social media platforms.
2. **Customer Support:** ensure that customers do not use hate speech when interacting with these chatbots.
3. **Content Recommendation Systems:** to avoid recommending content that contains hate speech.

# Pipeline Inplementation:


## Project Workflows
- constants
- config_enity
- artifact_enity
- components
- pipeline
- app.py



## How to run?

```bash
conda create -n hate python=3.8 -y
```

```bash
conda activate hate
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```


# Gcloud cli
https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe

```bash
gcloud init
```

## Deployment
1. Setting up circleCI
2. Switch on self hosted runner
3. Create Project
4. Configure EC2
5. config.yml
6. env variables
