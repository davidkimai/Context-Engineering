# The Garden Model: Cultivating Context  
花园模型：培育环境

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#the-garden-model-cultivating-context)

> _"A garden is a grand teacher. It teaches patience and careful watchfulness; it teaches industry and thrift; above all it teaches entire trust."  
> “花园是一位伟大的老师。它教会我们耐心和细心的观察；它教会我们勤劳和节俭；最重要的是，它教会我们完全的信任。”_
> 
> **— Gertrude Jekyll  — 格特鲁德·杰基尔**

## 1. Introduction: Why Think of Context as a Garden?  
1. 引言：为什么把环境想象成一座花园？

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#1-introduction-why-think-of-context-as-a-garden)

In our journey through context engineering, we've explored tokens, protocols, and field theory. Now, we turn to powerful mental models that make these abstract concepts intuitive and practical. The Garden Model is the first and perhaps most comprehensive of these frameworks.  
在上下文工程的探索过程中，我们探索了令牌、协议和场论。现在，我们转向强大的思维模型，它们使这些抽象概念变得直观且实用。花园模型是这些框架中第一个，或许也是最全面的一个。

Why a garden? Because context, like a garden, is:  
为什么是花园？因为环境就像花园一样，具有以下特点：

- **Living and evolving** - not static or fixed  
    **生存和发展** ——不是静止或固定的
- **Requiring cultivation** - needing deliberate care and attention  
    **需要栽培** ——需要刻意的照顾和关注
- **Organized but organic** - structured yet natural  
    **有序而有机** - 结构化而自然
- **Yielding in proportion to care** - reflecting the effort invested  
    **按关怀付出相应的回报** ——体现付出的努力
- **Balancing design and emergence** - combining intention with natural growth  
    **平衡设计与出现** ——将意图与自然生长相结合

The Garden Model provides a rich, intuitive framework for thinking about how to create, maintain, and evolve context in AI interactions.  
花园模型提供了一个丰富、直观的框架，用于思考如何在人工智能交互中创建、维护和发展环境。

**Socratic Question**: Think about gardens you've encountered in your life. What distinguishes a thriving garden from a neglected one? How might these same qualities apply to context in AI interactions?  
**苏格拉底式问题** ：想想你生活中遇到的花园。一个繁茂的花园和一个被忽视的花园有什么区别？这些相同的特质如何应用于人工智能交互的情境中？

```
┌─────────────────────────────────────────────────────────┐
│                THE GARDEN MODEL                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│       Design         Cultivation        Harvest         │
│      ────────        ──────────        ───────          │
│                                                         │
│    Planning the    Maintaining the    Reaping the       │
│    initial garden  growing context    benefits of       │
│    structure       elements           well-tended       │
│                                       context           │
│                                                         │
│    ┌───────────┐    ┌───────────┐    ┌───────────┐     │
│    │ Layout    │    │ Watering  │    │ Quality   │     │
│    │ Selection │    │ Weeding   │    │ Abundance │     │
│    │ Soil Prep │    │ Feeding   │    │ Variety   │     │
│    │ Pathways  │    │ Pruning   │    │ Timing    │     │
│    └───────────┘    └───────────┘    └───────────┘     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## 2. Garden Components and Context Parallels  
2. 花园组件和环境相似之处

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#2-garden-components-and-context-parallels)

The Garden Model maps garden elements directly to context engineering concepts:  
花园模型将花园元素直接映射到上下文工程概念：

### 2.1. Soil (Foundation)  2.1. 土壤（地基）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#21-soil-foundation)

In a garden, soil provides the foundation for all growth. In context:  
在花园里，土壤是所有植物生长的基础。上下文：

- **System Instructions**: The base soil that determines what can grow  
    **系统说明** ：决定什么可以生长的基础土壤
- **Token Budget**: The nutrient capacity of your soil  
    **代币预算** ：土壤的养分容量
- **Context Window**: The plot size of your garden  
    **上下文窗口** ：你的花园的地块大小
- **Core Values/Goals**: The soil pH and composition that influence everything  
    **核心价值观/目标** ：影响一切的土壤 pH 值和成分

```
/prepare.soil{
    instructions="clear, comprehensive, well-structured",
    token_efficiency="high nutrient density, low waste",
    value_alignment="balanced pH for desired growth",
    adaptability="well-aerated, responsive to change"
}
```

### 2.2. Seeds and Plants (Content)  
2.2. 种子和植物（内容）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#22-seeds-and-plants-content)

Gardens grow from carefully selected and placed plants. In context:  
花园的生长离不开精心挑选和栽种的植物。上下文：

- **Core Concepts**: Perennial plants that form the backbone  
    **核心概念** ：构成骨干的多年生植物
- **Examples**: Showcase specimens that demonstrate beauty and function  
    **示例** ：展示兼具美观和功能的标本
- **Key Information**: Productive plants that yield valuable harvests  
    **关键信息** ：高产植物，产出宝贵的收成
- **Questions/Prompts**: Seeds that catalyze new growth  
    **问题/提示** ：催化新生长的种子

```
/select.plants{
    core_concepts=[
        {type="perennial", role="structure", prominence="high"},
        {type="flowering", role="illustration", prominence="medium"},
        {type="productive", role="utility", prominence="high"}
    ],
    
    arrangement="complementary groupings",
    diversity="balanced for resilience",
    growth_pattern="supports intended development"
}
```

### 2.3. Layout (Structure)  2.3. 布局（结构）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#23-layout-structure)

Garden design creates order and flow. In context:  
花园设计营造秩序与流动。具体内容如下：

- **Information Architecture**: Garden beds and sections  
    **信息架构** ：花园床和部分
- **Conversation Flow**: Pathways through the garden  
    **对话流程** ：穿过花园的小径
- **Hierarchies**: Layers from canopy to ground cover  
    **层次结构** ：从冠层到地被植物的层
- **Relationships**: Companion planting and arrangements  
    **关系** ：伴生植物和安排

```
/design.layout{
    architecture=[
        {section="introduction", purpose="orientation", size="compact"},
        {section="exploration", purpose="discovery", size="expansive"},
        {section="application", purpose="utility", size="practical"},
        {section="conclusion", purpose="integration", size="reflective"}
    ],
    
    pathways="clear but not rigid",
    viewpoints="multiple perspectives offered",
    transitions="natural flow between sections"
}
```

### 2.4. Water and Nutrients (Resources)  
2.4. 水和营养物质（资源）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#24-water-and-nutrients-resources)

Gardens need ongoing resources. In context:  
花园需要持续的资源投入。具体如下：

- **Token Allocation**: Water supply for different areas  
    **代币分配** ：不同区域的供水
- **Examples/Details**: Nutrients for robust growth  
    **示例/详情** ：促进茁壮成长的营养素
- **Engagement**: Sunlight that energizes interaction  
    **参与** ：激发互动的阳光
- **Response Quality**: Overall resource richness  
    **响应质量** ：整体资源丰富度

```
/allocate.resources{
    token_distribution=[
        {area="foundation", allocation="sufficient but efficient"},
        {area="key_concepts", allocation="generous"},
        {area="examples", allocation="targeted"},
        {area="exploration", allocation="flexible reserve"}
    ],
    
    quality="high-value resources",
    timing="responsive to needs",
    efficiency="minimal waste"
}
```

### 2.5. Boundaries (Scope)  2.5. 边界（范围）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#25-boundaries-scope)

Gardens have edges that define their scope. In context:  
花园有边界，界定了它的范围。例如：

- **Topic Boundaries**: Garden walls and fences  
    **主题边界** ：花园围墙和栅栏
- **Scope Definition**: The overall garden size  
    **范围定义** ：整体花园规模
- **Relevance Filtering**: Gates and entry points  
    **相关性过滤** ：门和入口点
- **Focus Maintenance**: Garden borders and edge maintenance  
    **重点维护** ：花园边界和边缘维护

```
/establish.boundaries{
    scope="clearly defined but not rigid",
    entry_points="welcoming but controlled",
    borders="maintained but permeable",
    expansion_areas="designated for growth"
}
```

**Reflective Exercise**: Consider a recent AI interaction. How would you map its elements to a garden? What was the soil like? Which plants thrived, and which struggled? How was the layout structured? What might you change in your next "garden"?  
**反思练习** ：思考一下最近一次与人工智能的互动。你会如何将其元素映射到花园中？土壤是什么样的？哪些植物生长茂盛，哪些植物生长缓慢？花园的布局是怎样的？你会在下一个“花园”中做出哪些改变？

## 3. Garden Cultivation Practices  
3. 园林栽培实践

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#3-garden-cultivation-practices)

The heart of the Garden Model is the ongoing practices of cultivation that maintain and enhance context over time.  
花园模型的核心是持续的耕作实践，随着时间的推移维持和改善环境。

### 3.1. Planting (Initialization)  
3.1. 种植（初始化）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#31-planting-initialization)

How you start your garden sets the foundation for everything that follows:  
如何开始你的花园为接下来的一切奠定了基础：

```
/initialize.garden{
    preparation={
        clear_ground="remove irrelevant context",
        improve_soil="enhance foundation with key frameworks",
        plan_layout="design information architecture"
    },
    
    initial_planting={
        core_elements="essential concepts and definitions",
        structural_plants="organizing principles and frameworks",
        quick_yields="immediate-value examples and applications"
    },
    
    establishment_care={
        initial_watering="sufficient detail to start strong",
        protection="clear boundaries and focus",
        labeling="explicit signposting and navigation"
    }
}
```

### 3.2. Watering (Ongoing Nourishment)  
3.2. 浇水（持续滋养）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#32-watering-ongoing-nourishment)

Regular watering keeps your garden thriving:  
定期浇水可使您的花园蓬勃发展：

```
/nourish.context{
    regular_provision={
        depth="sufficient detail for understanding",
        frequency="responsive to complexity and needs",
        distribution="targeted to growth areas"
    },
    
    water_sources={
        examples="concrete illustrations",
        explanations="clear reasoning and connections",
        questions="thought-provoking inquiry"
    },
    
    efficiency={
        precision="directed to roots, not wasted",
        timing="when needed, not overwhelming",
        absorption="matched to processing capacity"
    }
}
```

### 3.3. Weeding (Pruning Irrelevance)  
3.3. 除草（剪除无关项）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#33-weeding-pruning-irrelevance)

Gardens require regular removal of elements that don't belong:  
花园需要定期清除不属于的元素：

```
/weed.context{
    identification={
        tangents="growth in wrong directions",
        redundancy="repetitive elements",
        outdated="no longer relevant information",
        harmful="elements that impede understanding"
    },
    
    removal_techniques={
        summarization="compress to essence",
        refocusing="redirect to core purpose",
        explicit_pruning="clear removal of unhelpful elements",
        boundary_reinforcement="prevent return of weeds"
    },
    
    timing={
        regular_maintenance="ongoing attention",
        seasonal_cleanup="periodic major review",
        responsive_intervention="immediate action when issues appear"
    }
}
```

### 3.4. Pruning (Refinement)  
3.4. 修剪（细化）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#34-pruning-refinement)

Strategic cutting back enhances health and productivity:  
战略性削减可增强健康和生产力：

```
/prune.for_growth{
    objectives={
        clarity="remove obscuring elements",
        focus="direct energy to priorities",
        rejuvenation="encourage fresh development",
        structure="maintain intended form"
    },
    
    techniques={
        token_reduction="trim wordiness",
        example_curation="select best instances",
        concept_sharpening="define more precisely",
        hierarchy_reinforcement="clarify relationships"
    },
    
    approach={
        deliberate="thoughtful, not reactive",
        preservative="maintain valuable aspects",
        growth_oriented="cut to stimulate, not diminish"
    }
}
```

### 3.5. Fertilizing (Enrichment)  
3.5. 施肥（强化）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#35-fertilizing-enrichment)

Adding nutrients enhances garden vitality:  
添加营养物质可增强花园活力：

```
/enrich.context{
    nutrients={
        examples="illustrative scenarios",
        analogies="comparative insights",
        data="supporting evidence",
        perspectives="alternative viewpoints"
    },
    
    application={
        targeted="where most needed",
        balanced="complementary elements",
        timed="when most receptive"
    },
    
    integration={
        absorption="connecting to existing knowledge",
        distribution="spreading throughout relevant areas",
        transformation="converting to usable understanding"
    }
}
```

**Socratic Question**: Which of these garden cultivation practices do you currently employ most effectively in your context engineering? Which might benefit from more attention? How would focusing on a neglected practice change your results?  
**苏格拉底式问题** ：在您的上下文工程中，您目前最有效地采用了哪些园林栽培实践？哪些实践可能需要更多关注？关注那些被忽视的实践会如何改变您的结果？

## 4. Garden Varieties (Context Types)  
4. 普通品种（上下文类型）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#4-garden-varieties-context-types)

Different goals call for different types of gardens, each with distinct characteristics:  
不同的目标需要不同类型的花园，每种花园都有不同的特点：

### 4.1. The Kitchen Garden (Utility-Focused Context)  
4.1. 厨房花园（以实用性为中心的环境）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#41-the-kitchen-garden-utility-focused-context)

Optimized for practical output and utility:  
针对实际输出和实用性进行了优化：

```
/design.kitchen_garden{
    purpose="practical, outcome-oriented interaction",
    
    characteristics={
        productivity="high yield of useful results",
        efficiency="minimal waste, maximum utility",
        organization="clear, functional layout",
        accessibility="easy to harvest results"
    },
    
    typical_elements={
        frameworks="reliable production methods",
        examples="proven, productive varieties",
        processes="step-by-step instructions",
        evaluation="quality assessment methods"
    },
    
    maintenance={
        focus="yield and functionality",
        cycle="regular harvesting and replanting",
        expansion="based on utility and demand"
    }
}
```

Examples: Task-specific assistants, problem-solving contexts, procedural guidance  
示例：特定任务助手、问题解决情境、程序指导

### 4.2. The Formal Garden (Structured Context)  
4.2. 正式花园（结构化环境）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#42-the-formal-garden-structured-context)

Emphasizes clear organization, precision, and order:  
强调清晰的组织、精确和秩序：

```
/design.formal_garden{
    purpose="precise, structured interaction",
    
    characteristics={
        order="clear hierarchies and categories",
        precision="exact definitions and boundaries",
        symmetry="balanced presentation of information",
        predictability="consistent patterns and frameworks"
    },
    
    typical_elements={
        taxonomies="precise classification systems",
        principles="fundamental rules and patterns",
        criteria="clear standards for evaluation",
        procedures="exact sequences and methods"
    },
    
    maintenance={
        focus="preserving structure and clarity",
        cycle="regular reinforcement of patterns",
        expansion="symmetrical and planned growth"
    }
}
```

Examples: Educational contexts, technical documentation, analytical frameworks  
示例：教育背景、技术文档、分析框架

### 4.3. The Cottage Garden (Creative Context)  
4.3. 小屋花园（创意背景）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#43-the-cottage-garden-creative-context)

Designed for exploration, creativity, and unexpected connections:  
专为探索、创造力和意想不到的联系而设计：

```
/design.cottage_garden{
    purpose="creative, generative interaction",
    
    characteristics={
        diversity="wide variety of elements",
        spontaneity="room for unexpected connections",
        abundance="rich, overflowing resources",
        charm="engaging, delightful experience"
    },
    
    typical_elements={
        inspirations="diverse creative sparks",
        possibilities="open-ended explorations",
        associations="unexpected connections",
        variations="multiple expressions of ideas"
    },
    
    maintenance={
        focus="nurturing creativity and surprise",
        cycle="seasonal refreshment and change",
        expansion="organic, opportunistic growth"
    }
}
```

Examples: Brainstorming contexts, creative writing, artistic collaboration  
示例：头脑风暴情境、创意写作、艺术合作

### 4.4. The Zen Garden (Minimalist Context)  
4.4. 禅宗花园（极简主义语境）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#44-the-zen-garden-minimalist-context)

Focused on simplicity, mindfulness, and essence:  
注重简单、正念和本质：

```
/design.zen_garden{
    purpose="clarity, focus, and essence",
    
    characteristics={
        simplicity="reduced to what matters most",
        space="room for reflection and processing",
        focus="clear central elements",
        subtlety="nuance within simplicity"
    },
    
    typical_elements={
        core_principles="fundamental truths",
        essential_questions="key inquiries",
        space="deliberate emptiness",
        mindful_presentation="carefully chosen elements"
    },
    
    maintenance={
        focus="continuous refinement and reduction",
        cycle="regular reassessment of necessity",
        expansion="only when absolutely essential"
    }
}
```

Examples: Philosophical exploration, deep focus on single concepts, meditative contexts  
示例：哲学探索、深入关注单一概念、冥想情境

**Reflective Exercise**: Which garden variety best describes your typical context approach? What would change if you intentionally designed your next interaction as a different garden type? How might a Zen Garden approach differ from a Cottage Garden approach for the same topic?  
**反思练习** ：哪种花园类型最能体现你典型的情境方法？如果你有意将下一次互动设计成另一种花园类型，会发生什么变化？对于同一主题，禅意花园与小屋花园会有何不同？

## 5. Garden Seasons (Context Evolution)  
5. 花园四季（背景演变）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#5-garden-seasons-context-evolution)

Gardens change with the seasons, and so do contexts over time:  
花园随着季节而变化，环境也随着时间而变化：

### 5.1. Spring (Initialization)  
5.1. Spring（初始化）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#51-spring-initialization)

The season of new beginnings and rapid growth:  
新的开始和快速成长的季节：

```
/navigate.spring{
    characteristics={
        energy="high engagement and exploration",
        growth="rapid development of new elements",
        flexibility="direction still being established",
        experimentation="trying different approaches"
    },
    
    activities={
        planting="establishing core concepts",
        planning="laying out key directions",
        preparation="building foundational understanding",
        protection="guarding against early confusion"
    },
    
    focus="potential and direction"
}
```

### 5.2. Summer (Development)  
5.2. 夏季（开发）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#52-summer-development)

The season of full growth and productivity:  
充分生长和生产丰收的季节：

```
/navigate.summer{
    characteristics={
        abundance="rich development of ideas",
        maturity="fully formed concepts",
        productivity="high output and application",
        visibility="clear manifestation of intentions"
    },
    
    activities={
        tending="maintaining momentum and direction",
        harvesting="gathering insights and applications",
        protecting="preventing disruption of productivity",
        sharing="leveraging abundant resources"
    },
    
    focus="production and fulfillment"
}
```

### 5.3. Autumn (Harvest)  5.3. 秋季（收获）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#53-autumn-harvest)

The season of gathering value and preparing for transition:  
积累价值和准备过渡的季节：

```
/navigate.autumn{
    characteristics={
        integration="bringing elements together",
        assessment="evaluating what has grown",
        selection="identifying what to preserve",
        preparation="getting ready for next phase"
    },
    
    activities={
        harvesting="collecting key insights and results",
        preserving="documenting valuable outcomes",
        distilling="extracting essential lessons",
        planning="considering future directions"
    },
    
    focus="consolidation and evaluation"
}
```

### 5.4. Winter (Rest and Renewal)  
5.4. 冬季（休息和恢复）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#54-winter-rest-and-renewal)

The season of dormancy, reflection, and planning:  
休眠、反思和计划的季节：

```
/navigate.winter{
    characteristics={
        stillness="reduced activity",
        clarity="stripped to essentials",
        reflection="deeper consideration",
        potential="latent future directions"
    },
    
    activities={
        assessment="reviewing the complete cycle",
        planning="designing for new growth",
        clearing="removing what's no longer needed",
        preparation="readying for new beginnings"
    },
    
    focus="reflection and renewal"
}
```

### 5.5. Perennial Contexts  5.5. 永恒背景

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#55-perennial-contexts)

Some contexts are designed to last through multiple seasons:  
有些情境被设计为可以持续多个季节：

```
/design.perennial_context{
    characteristics={
        persistence="maintains value over time",
        adaptation="adjusts to changing conditions",
        renewal="refreshes without complete restart",
        evolution="develops rather than replacing"
    },
    
    strategies={
        core_stability="maintain essential elements",
        seasonal_adjustment="adapt to changing needs",
        regular_renewal="refresh key components",
        selective_preservation="maintain what works"
    },
    
    implementation={
        baseline_maintenance="ongoing care of fundamentals",
        adaptive_elements="flexible components that evolve",
        seasonal_review="regular assessment and adjustment",
        growth_rings="layered development over time"
    }
}
```

**Socratic Question**: Where in the seasonal cycle are your current context projects? How might recognizing the appropriate season change how you approach them? What happens when you try to force summer productivity during a winter phase?  
**苏格拉底式问题** ：你目前的项目处于季节周期的哪个阶段？识别合适的季节会如何影响你处理这些项目的方式？当你试图在冬季阶段强制进行夏季生产时会发生什么？

## 6. Garden Problems and Solutions  
6. 花园问题及解决方案

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#6-garden-problems-and-solutions)

Even well-designed gardens face challenges. Here's how to address common issues:  
即使是精心设计的花园也会面临挑战。以下是一些常见问题的解决方法：

### 6.1. Overgrowth (Information Overload)  
6.1. 过度增长（信息超载）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#61-overgrowth-information-overload)

When your garden becomes too dense and crowded:  
当你的花园变得过于密集和拥挤时：

```
/address.overgrowth{
    symptoms={
        token_saturation="approaching or exceeding limits",
        cognitive_overload="too much to process clearly",
        loss_of_focus="key elements obscured by details",
        diminishing_returns="additional elements add little value"
    },
    
    solutions={
        aggressive_pruning="remove non-essential elements",
        prioritization="identify and highlight key components",
        restructuring="organize for clarity and efficiency",
        segmentation="divide into manageable sections"
    },
    
    prevention={
        regular_maintenance="ongoing evaluation and pruning",
        disciplined_addition="careful consideration before including new elements",
        clear_pathways="maintain navigational clarity"
    }
}
```

### 6.2. Weeds (Irrelevance and Tangents)  
6.2. 杂草（无关内容和离题内容）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#62-weeds-irrelevance-and-tangents)

When unwanted elements threaten to take over:  
当不受欢迎的因素威胁要接管时：

```
/address.weeds{
    symptoms={
        topic_drift="conversation moving away from purpose",
        irrelevant_details="information that doesn't serve goals",
        unhelpful_patterns="recurring distractions",
        crowding_out="valuable elements lost among irrelevance"
    },
    
    solutions={
        targeted_removal="eliminate specific irrelevant elements",
        boundary_reinforcement="clarify and strengthen topic borders",
        refocusing="explicitly return to core purpose",
        soil_improvement="strengthen foundational instructions"
    },
    
    prevention={
        clear_boundaries="well-defined scope from the beginning",
        regular_weeding="address small issues before they grow",
        mulching="protective layer of clarity around key concepts"
    }
}
```

### 6.3. Drought (Resource Scarcity)  
6.3. 干旱（资源稀缺）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#63-drought-resource-scarcity)

When your garden lacks necessary resources:  
当您的花园缺乏必要的资源时：

```
/address.drought{
    symptoms={
        token_starvation="insufficient space for proper development",
        shallow_understanding="lack of depth in key areas",
        withering_concepts="important ideas failing to develop",
        productivity_drop="declining quality of outputs"
    },
    
    solutions={
        resource_prioritization="direct tokens to most important elements",
        efficiency_techniques="do more with available resources",
        drought-resistant_planning="design for low-resource conditions",
        strategic_irrigation="targeted provision to essential areas"
    },
    
    prevention={
        resource_planning="anticipate needs before beginning",
        efficient_design="create with constraints in mind",
        drought-tolerant_selection="choose elements that thrive with less"
    }
}
```

### 6.4. Pests and Diseases (Disruptions)  
6.4. 病虫害（干扰）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#64-pests-and-diseases-disruptions)

When harmful elements threaten garden health:  
当有害因素威胁花园健康时：

```
/address.disruptions{
    symptoms={
        misunderstanding="communication breakdowns",
        confusion="unclear or contradictory elements",
        derailment="conversation knocked off intended path",
        quality_issues="deteriorating outputs"
    },
    
    solutions={
        isolation="contain problematic elements",
        treatment="directly address specific issues",
        reinforcement="strengthen weakened areas",
        reset="clear restart if necessary"
    },
    
    prevention={
        healthy_foundation="strong, clear initial structure",
        diversity="varied approaches for resilience",
        regular_monitoring="catch issues early",
        protective_practices="design to minimize vulnerabilities"
    }
}
```

**Reflective Exercise**: What garden problems have you encountered in your context engineering work? How did you address them? Which preventative measures might help you avoid similar issues in the future?  
**反思练习** ：你在上下文工程工作中遇到了哪些花园问题？你是如何解决的？哪些预防措施可以帮助你避免将来再次出现类似的问题？

## 7. Garden Tools (Context Engineering Techniques)  
7. 园艺工具（上下文工程技术）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#7-garden-tools-context-engineering-techniques)

Every gardener needs the right tools. Here are key techniques mapped to garden implements:  
每个园丁都需要合适的工具。以下是与园艺工具相关的关键技巧：

### 7.1. Spade and Trowel (Foundational Tools)  
7.1. 铲子和泥刀（基础工具）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#71-spade-and-trowel-foundational-tools)

For establishing the garden's foundation:  
建立花园的基础：

```
/use.foundational_tools{
    techniques=[
        {
            name="clear instruction design",
            function="establish solid foundation",
            application="beginning of interaction",
            example="/system.instruct{role='expert gardener', approach='permaculture principles'}"
        },
        {
            name="concept definition",
            function="prepare ground for understanding",
            application="introducing key elements",
            example="/define.precisely{concept='companion planting', scope='within this garden context'}"
        },
        {
            name="scope delineation",
            function="mark garden boundaries",
            application="establishing focus and limits",
            example="/boundary.set{include=['annual planning', 'plant selection'], exclude=['long-term landscape design']}"
        }
    ]
}
```

### 7.2. Watering Can and Hose (Nourishment Tools)  
7.2. 喷壶和软管（营养工具）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#72-watering-can-and-hose-nourishment-tools)

For providing essential resources:  
提供必要资源：

```
/use.nourishment_tools{
    techniques=[
        {
            name="example provision",
            function="targeted resource delivery",
            application="illustrating concepts",
            example="/example.provide{concept='plant spacing', specific='tomato planting at 24-inch intervals'}"
        },
        {
            name="explanation expansion",
            function="deep watering for strong roots",
            application="ensuring fundamental understanding",
            example="/explain.depth{topic='soil composition', detail_level='comprehensive but practical'}"
        },
        {
            name="question irrigation",
            function="stimulating growth through inquiry",
            application="encouraging deeper exploration",
            example="/question.explore{area='seasonal adaptation', approach='socratic'}"
        }
    ]
}
```

### 7.3. Pruners and Shears (Refinement Tools)  
7.3. 修枝剪和剪刀（精炼工具）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#73-pruners-and-shears-refinement-tools)

For shaping and maintaining:  
用于塑造和维护：

```
/use.refinement_tools{
    techniques=[
        {
            name="summarization",
            function="pruning for clarity and focus",
            application="reducing overgrowth",
            example="/summarize.key_points{content='detailed planting discussion', focus='actionable insights'}"
        },
        {
            name="precision editing",
            function="careful shaping for form",
            application="refining specific elements",
            example="/edit.precise{target='watering guidelines', for='clarity and actionability'}"
        },
        {
            name="restructuring",
            function="major reshaping for health",
            application="improving overall organization",
            example="/restructure.for_flow{content='seasonal planning guide', pattern='chronological'}"
        }
    ]
}
```

### 7.4. Compass and Measuring Tape (Assessment Tools)  
7.4. 圆规和卷尺（评估工具）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#74-compass-and-measuring-tape-assessment-tools)

For evaluation and planning:  
对于评估和规划：

```
/use.assessment_tools{
    techniques=[
        {
            name="quality evaluation",
            function="measuring growth and health",
            application="assessing current state",
            example="/evaluate.quality{output='garden plan', criteria=['completeness', 'practicality', 'clarity']}"
        },
        {
            name="gap analysis",
            function="identifying missing elements",
            application="planning improvements",
            example="/analyze.gaps{current='plant selection guide', desired='comprehensive seasonal planting reference'}"
        },
        {
            name="alignment check",
            function="ensuring proper orientation",
            application="verifying direction",
            example="/check.alignment{content='garden design', goals='low-maintenance productive garden'}"
        }
    ]
}
```

**Socratic Question**: Which garden tools do you use most comfortably in your context engineering? Which might you benefit from incorporating more intentionally? How could developing skill with an underutilized tool expand your capabilities?  
**苏格拉底式问题** ：在你的工程实践中，你最擅长使用哪些园艺工具？哪些工具可以让你更有意识地融入其中？如何利用这些未被充分利用的工具来提升你的技能？

## 8. The Gardener's Mindset  
8. 园丁的心态

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#8-the-gardeners-mindset)

Beyond techniques and structures, successful context gardening requires cultivating certain attitudes and approaches:  
除了技术和结构之外，成功的环境园艺还需要培养某些态度和方法：

### 8.1. Patience  8.1. 耐心

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#81-patience)

Gardens unfold in their own time:  
花园按照自己的时间展开：

```
/cultivate.patience{
    understanding={
        natural_timing="respecting development cycles",
        incremental_growth="valuing small, consistent progress",
        long_view="seeing beyond immediate results"
    },
    
    practices={
        phased_expectations="setting realistic timelines",
        milestone_celebration="acknowledging progress points",
        process_appreciation="finding value in the journey"
    },
    
    benefits={
        reduced_frustration="accepting natural rhythms",
        deeper_development="allowing full maturation",
        sustainable_approach="preventing burnout"
    }
}
```

### 8.2. Attentiveness  8.2. 专注力

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#82-attentiveness)

Successful gardeners notice what others miss:  
成功的园丁会注意到别人所忽略的东西：

```
/cultivate.attentiveness{
    understanding={
        present_awareness="being fully engaged with current state",
        pattern_recognition="noticing recurring elements and trends",
        subtle_signals="detecting early indicators of issues or opportunities"
    },
    
    practices={
        regular_observation="consistent, intentional assessment",
        multi-level_scanning="checking different layers and aspects",
        reflective_pauses="creating space for noticing"
    },
    
    benefits={
        early_intervention="addressing issues before they grow",
        opportunity_recognition="seeing possibilities others miss",
        deeper_connection="understanding nuances and subtleties"
    }
}
```

### 8.3. Adaptability  8.3. 适应性

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#83-adaptability)

Gardens require flexibility and responsiveness:  
花园需要灵活性和响应能力：

```
/cultivate.adaptability{
    understanding={
        living_systems="recognizing organic, unpredictable nature",
        environmental_interaction="acknowledging external influences",
        evolutionary_development="embracing change as natural"
    },
    
    practices={
        responsive_adjustment="changing approach based on results",
        experimental_mindset="trying different methods",
        assumption_questioning="revisiting established patterns"
    },
    
    benefits={
        resilience="thriving despite challenges",
        continuous_improvement="evolving rather than stagnating",
        opportunity_leverage="turning changes into advantages"
    }
}
```

### 8.4. Stewardship  8.4. 管理职责

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#84-stewardship)

Gardeners serve the garden, not just themselves:  
园丁不仅为自己服务，还为花园服务：

```
/cultivate.stewardship{
    understanding={
        ecological_view="seeing interconnections and whole systems",
        service_orientation="focusing on garden needs, not just desires",
        future_thinking="considering long-term impacts"
    },
    
    practices={
        sustainable_methods="approaches that maintain health over time",
        balanced_intervention="knowing when to act and when to observe",
        resource_responsibility="using inputs wisely and efficiently"
    },
    
    benefits={
        garden_thriving="overall health and vitality",
        sustainable_productivity="lasting rather than depleting results",
        satisfaction="deeper fulfillment from appropriate care"
    }
}
```

**Reflective Exercise**: Which gardener's mindset quality comes most naturally to you? Which requires more intentional development? How might strengthening a challenging mindset quality change your context engineering approach?  
**反思练习** ：哪种园丁心态对你来说最自然？哪种需要更有意识地培养？强化挑战性心态会如何改变你的上下文工程方法？

## 9. Garden Design Patterns  
9.花园设计模式

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#9-garden-design-patterns)

These integrated patterns combine multiple garden elements into cohesive approaches:  
这些综合模式将多种园林元素结合成具有凝聚力的方法：

### 9.1. The Kitchen Garden Pattern  
9.1. 厨房花园模式

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#91-the-kitchen-garden-pattern)

For practical, productive contexts:  
对于实际、高效的环境：

```
/implement.kitchen_garden{
    design={
        layout="organized for efficient access and harvest",
        elements="selected for productivity and utility",
        proportions="balanced for consistent yield"
    },
    
    cultivation={
        planting="direct instruction and clear examples",
        maintenance="regular pruning for clarity and focus",
        harvesting="explicit collection of valuable outputs"
    },
    
    application={
        technical_documentation="practical knowledge gardens",
        procedural_guidance="step-by-step instruction contexts",
        problem_solving="solution-oriented environments"
    }
}
```

### 9.2. The Contemplative Garden Pattern  
9.2. 沉思花园模式

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#92-the-contemplative-garden-pattern)

For reflective, insight-oriented contexts:  
对于反思性、洞察力导向的背景：

```
/implement.contemplative_garden{
    design={
        layout="spacious, with room for reflection",
        elements="selected for depth and meaning",
        proportions="balanced between content and space"
    },
    
    cultivation={
        planting="thought-provoking questions and concepts",
        maintenance="gentle guidance rather than strict control",
        harvesting="recognition and integration of insights"
    },
    
    application={
        philosophical_exploration="concept gardens",
        personal_development="growth-oriented contexts",
        creative_contemplation="inspiration environments"
    }
}
```

### 9.3. The Educational Garden Pattern  
9.3 教育花园模式

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#93-the-educational-garden-pattern)

For learning and skill development contexts:  
对于学习和技能发展环境：

```
/implement.educational_garden{
    design={
        layout="progressive path from basics to advanced",
        elements="selected for learning value and progression",
        proportions="balanced between instruction and practice"
    },
    
    cultivation={
        planting="foundational concepts with clear examples",
        maintenance="scaffolded support with gradual release",
        harvesting="demonstration of understanding and application"
    },
    
    application={
        skill_development="practice-oriented gardens",
        knowledge_building="conceptual framework contexts",
        mastery_progression="expertise development environments"
    }
}
```

### 9.4. The Collaborative Garden Pattern  
9.4 合作花园模式

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#94-the-collaborative-garden-pattern)

For shared creation and co-development contexts:  
对于共享创作和共同开发环境：

```
/implement.collaborative_garden{
    design={
        layout="open spaces with shared areas",
        elements="complementary contributions from multiple sources",
        proportions="balanced voices and perspectives"
    },
    
    cultivation={
        planting="invitation for diverse inputs",
        maintenance="integration and harmonization of elements",
        harvesting="recognition of collective creation"
    },
    
    application={
        co_creation="shared project gardens",
        diverse_perspective="multi-viewpoint contexts",
        community_development="collective growth environments"
    }
}
```

**Socratic Question**: Which garden design pattern most closely aligns with your current needs? How might deliberately choosing and implementing a specific pattern change your approach to an upcoming project?  
**苏格拉底式问题** ：哪种花园设计模式最符合您当前的需求？精心选择并实施一个特定的模式会如何改变您接下来的项目方法？

## 10. Conclusion: Becoming a Master Gardener  
10. 结论：成为园艺大师

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/NOCODE/10_mental_models/01_garden_model.md#10-conclusion-becoming-a-master-gardener)

Context engineering through the Garden Model is not just a technique but an ongoing practice and mindset. As you develop your gardening skills, you'll move from simply following instructions to developing an intuitive sense for what works in different situations.  
通过花园模型进行上下文工程不仅仅是一门技术，更是一种持续的实践和思维方式。随着园艺技能的提升，你将从简单的遵循指示，发展出一种直觉，能够在不同情况下找到最佳方案。

The journey to mastery involves:  
通往精通的旅程包括：

1. **Regular practice** - tending many different gardens  
    **定期练习** ——照料许多不同的花园
2. **Thoughtful reflection** - learning from successes and challenges  
    **深思熟虑的反思** ——从成功和挑战中学习
3. **Pattern recognition** - seeing common elements across diverse contexts  
    **模式识别** ——在不同的背景下发现共同元素
4. **Adaptive expertise** - knowing when to follow rules and when to break them  
    **适应性专业知识** ——知道何时遵守规则，何时打破规则
5. **Community engagement** - learning from and contributing to other gardeners  
    **社区参与** ——向其他园丁学习并做出贡献

As you continue your context engineering journey, let the Garden Model serve as both a practical framework and an inspirational metaphor. Your gardens will become more beautiful, productive, and sustainable with each cycle of growth.  
在您继续上下文工程之旅的过程中，让花园模型既成为实用的框架，又成为鼓舞人心的隐喻。随着每个生长周期的推进，您的花园将变得更加美丽、更加丰饶、更加可持续。

**Final Reflective Exercise**: Envision the next context "garden" you want to create. What type will it be? What will you plant? How will you tend it? What do you hope to harvest? What lesson from this guide will you apply most deliberately?  
**最后的反思练习** ：设想一下你想创建的下一个“花园”。它会是什么类型的？你会种什么？你会如何照料它？你希望收获什么？你会最有意识地运用本指南中的哪些经验？

---

> _"If you have a garden and a library, you have everything you need."  
> “如果你有一个花园和一个图书馆，你就拥有了你需要的一切。”_
> 
> **— Cicero  — 西塞罗**