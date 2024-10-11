# Prompt

Great work I'm building up a demo Obsidian vault which shows how I use Obsidian to store LLM outputs. You might have some details about my actual vault in context. Can you suggest some dummy data and folders I can create to give a complete picture of how this approach can be used

# Output

Certainly! I'll suggest some **folders**, **dummy data**, and **notes** that can illustrate how you use Obsidian to organize LLM (Large Language Model) outputs. I’ll keep the approach cohesive, similar to how you might actually be using it, based on your preferences.

Here’s a suggested structure for a **demo Obsidian vault**:

### Vault Folder Structure:
1. **Context** (folder)
2. **Prompts** (folder)
3. **Outputs** (folder)
   - **Raw** (sub-folder)
   - **Refined** (sub-folder)
4. **Agents** (folder)
5. **Resources** (folder)
6. **Research** (folder)
7. **Follow-Ups** (folder)

Let me break down each folder and provide **dummy data** ideas for them:

#### 1. **Context** (Folder)
The "Context" folder is where you save pieces of context information that you use to prime your LLM for more relevant and detailed responses. Here are some ideas for context snippets:

- **File Name**: `Project_Background.md`
  - **Content**:
    ```markdown
    # Project Background

    This project focuses on developing communication strategies for environmental advocacy. It involves engaging with both the public and government bodies to raise awareness about sustainability initiatives.
    ```

- **File Name**: `Personal_Background.md`
  - **Content**:
    ```markdown
    # Personal Background

    I'm a communications strategist working primarily in the field of environmental projects. My background includes digital content creation, data-driven storytelling, and public advocacy.
    ```

- **File Name**: `Organization_Goals.md`
  - **Content**:
    ```markdown
    # Organization Goals

    The primary goal is to develop public engagement campaigns that promote environmental sustainability and foster positive behavioral changes, including reducing plastic use and promoting recycling initiatives.
    ```

#### 2. **Prompts** (Folder)
The "Prompts" folder stores prompts that you reuse for LLM interactions.

- **File Name**: `Content_Strategy_Prompt.md`
  - **Content**:
    ```markdown
    # Prompt

    Develop a content strategy for a campaign aimed at reducing single-use plastic. The strategy should include ideas for social media, blog posts, and community engagement.
    ```

- **File Name**: `Product_Launch_Prompt.md`
  - **Content**:
    ```markdown
    # Prompt

    Create a launch plan for a new eco-friendly water bottle. Include messaging ideas and engagement strategies for different target audiences (students, professionals, families).
    ```

#### 3. **Outputs** (Folder)
This is where the LLM-generated outputs are saved. I suggest splitting these into **Raw** and **Refined** subfolders.

- **Raw** (Sub-folder): This contains direct outputs from the LLM.
  - **File Name**: `Reducing_Plastic_Raw.md`
    - **Content**:
      ```markdown
      # Prompt

      How can communities reduce plastic use?

      # Output

      Communities can reduce plastic use by organizing local events focused on raising awareness, setting up accessible recycling points, and encouraging stores to eliminate plastic bags by providing incentives for reusable alternatives.
      ```

- **Refined** (Sub-folder): This contains edited and refined versions of the raw outputs for better readability or further use.
  - **File Name**: `Reducing_Plastic_Refined.md`
    - **Content**:
      ```markdown
      # Prompt

      How can communities reduce plastic use?

      # Refined Output

      Communities can reduce plastic use through:
      
      1. **Awareness Campaigns**: Host local workshops to educate residents on the dangers of plastic pollution.
      2. **Recycling Points**: Increase the number of accessible recycling facilities.
      3. **Reusable Incentives**: Encourage local stores to promote reusable bags through discounts or loyalty points.
      ```

#### 4. **Agents** (Folder)
This folder stores configurations for different custom LLM agents you've created.

- **File Name**: `Campaign_Agent_Config.json`
  - **Content**:
    ```json
    {
      "name": "Campaign Agent",
      "description": "Specializes in generating content strategies for environmental advocacy campaigns.",
      "temperature": 0.7,
      "tone": "Informative",
      "context": "Focus on sustainability and behavioral change"
    }
    ```

- **File Name**: `Research_Agent_Config.json`
  - **Content**:
    ```json
    {
      "name": "Research Agent",
      "description": "Designed to gather information and synthesize research on environmental policy.",
      "temperature": 0.3,
      "tone": "Analytical",
      "context": "Detailed, research-focused answers about environmental issues"
    }
    ```

#### 5. **Resources** (Folder)
The "Resources" folder contains reference materials and key documents that can help add value to LLM outputs.

- **File Name**: `Plastic_Impact_Stats.md`
  - **Content**:
    ```markdown
    # Plastic Impact Statistics

    - Every year, more than 8 million tons of plastic end up in the ocean.
    - It takes approximately 450 years for a plastic bottle to degrade.
    - Single-use plastics make up 50% of the plastic we use.
    ```

- **File Name**: `Climate_Change_Report.md`
  - **Content**:
    ```markdown
    # Key Insights from Climate Change Report 2024

    - Global temperatures have increased by 1.1°C since the pre-industrial era.
    - CO2 emissions are currently at their highest recorded level.
    - Developing nations are facing disproportionate impacts, with higher rates of extreme weather events.
    ```

#### 6. **Research** (Folder)
This folder can hold deeper dives into various topics, often generated through iterative LLM queries.

- **File Name**: `Plastic_Waste_Research.md`
  - **Content**:
    ```markdown
    # Research on Plastic Waste Reduction

    The research focuses on community-led initiatives that have been successful in reducing plastic use:
    - **Freiburg, Germany**: Introduced a city-wide ban on plastic bags, which led to a 60% reduction in plastic waste.
    - **Kerala, India**: Local women-led groups began producing biodegradable alternatives to plastic, reducing neighborhood plastic pollution.
    ```

- **File Name**: `Behavioral_Change_Research.md`
  - **Content**:
    ```markdown
    # Research on Behavioral Change in Sustainability

    Behavioral change is key to fostering sustainability:
    - **Incentives**: Reward-based systems are highly effective in increasing recycling rates.
    - **Education**: Early school education about environmental stewardship leads to more responsible adults.
    - **Social Norms**: Public commitment and peer influence significantly impact recycling habits.
    ```

#### 7. **Follow-Ups** (Folder)
The "Follow-Ups" folder is where you keep notes on tasks or important actions to revisit later, based on LLM outputs.

- **File Name**: `Plastic_Campaign_FollowUps.md`
  - **Content**:
    ```markdown
    # Follow-Ups for Plastic Reduction Campaign

    - [ ] Contact local artists about creating public murals for awareness.
    - [ ] Set up a meeting with community leaders to discuss the introduction of recycling incentives.
    - [ ] Draft a social media post plan focusing on "Plastic-Free July."
    ```

- **File Name**: `Website_Content_Update.md`
  - **Content**:
    ```markdown
    # Website Content Update Follow-Ups

    - [ ] Review and refine the 'About Us' section to reflect recent projects.
    - [ ] Add statistics from the latest sustainability report to the homepage.
    - [ ] Update the "Get Involved" section with upcoming community event dates.
    ```

---

### Overall Workflow Demonstration:
The folders and files help demonstrate a logical workflow that incorporates **LLM outputs into actionable content**:
1. **Context** files are saved to provide the background for generating more relevant LLM outputs.
2. **Prompts** are used for consistency across multiple requests, ensuring refined outputs.
3. **Outputs** are organized as "Raw" and "Refined" to show the iterative process of editing LLM-generated content.
4. **Agents** are customized LLM configurations, each suited for specific purposes, saved in a structured way.
5. **Resources** hold the necessary background information, references, and key statistics used to make the LLM responses more informed.
6. **Research** documents contain the deeper dive content, often developed in collaboration with the LLM.
7. **Follow-Ups** provide actionable next steps based on the outputs, making it clear how the LLM is impacting day-to-day tasks.

---

I hope this structure helps you showcase the potential of using Obsidian to organize LLM outputs and related workflows! If you need more folders or examples, or if you'd like to focus on specific use cases, just let me know!
