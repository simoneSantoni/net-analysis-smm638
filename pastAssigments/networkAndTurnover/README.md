# Case study 2 – Mobility and intra-organizational networks

<center><img src='images/retention.jpg' width=600px /></center>

# Introduction

Professional service firms are characterized by high levels of turnover. Several factors account for personnel churn. For example: a) geographic clustering – professional service firms' presence is concentrated in urban areas if not specific boroughs: this makes mobility relatively inexpensive from an individual standpoint; b) professional service markets show the typical oligopoly form wherein a few actors of comparable size fiercely compete for customers and resources, including talented knowledge workers; c) poor HR management practices, which generate attrition.

Irrespective of the causes, recurrent personnel churn threatens the organizational performance of professional service firms, and, ultimately the possibility to get and to sustain a favorable/competitive advantage position in the reference sector (see the 'Resource Based View of the Firm' literature[1]). Hence, top managers of professional service firms should carefully analyze the implications of 'letting an employee go.

# Context for the case study

According to the prior literature and empirical evidence, personnel churn is associated with several inter-personal and organizational processes[2]. Ultimately, such channels can be grouped with respect to the :

- __human capital loss__: talented individuals are hard to replace!
- __social capital loss__: inter-personal, informal inter-personnel interactions are key to promote organizational effectiveness. This is particularly true in the context of professional service firms, wherein 'tasks' always entail some level of uncertainty, and, therefore, are impossible to standardize or to fully describe in organizational procedures. In such a scenario, the informal network that emerges out the spontaneous interactions among employees is a coordination mechanism that complements formal procedures, roles, and organizational/reporting structures. Every mobility event stresses the informal network and, as a result, negatively affects outcomes such as:
  * group-level information processing, which depends on network connectivity
  * inter-personal knowledge exchange, which largely flows through strong ties (think about a mentoring relationship)
  * leadership and inter-personal/group-level coordination

Prior studies have started to articulate the role communities of enthusiasts can play in promoting category creating products. However, we have a very limited knowledge of how innovators can leverage upon these communities, possibly, just a few individuals, to sustain the diffusion of their innovations.

# Problem to address

⍺βƔ is a prominent law firm based in Europe, which counts circa 1,000 associates and 200 partner attorneys and operates in the business segment. Over the past five years, ⍺βƔ has been coping with a high number of voluntary mobility events that were mainly due to competitive offers from rival firms. In a fraction of the cases, employees were retained by matching rivals' offers. Executives have started to consider churn a structural feature of the sector – hence, they have planned to create some policies aiming at minimizing the negative impact of mobility and ensuring consistency across mobility cases. Use [this dataset](https://drive.google.com/drive/folders/1Vs2-P450i3CzmvH68n9YuuK-jVpV9vW5?usp=sharing) containing relational and attributive data on attorneys (companion documents included in the folder), to address the below-displayed questions:

- what are the key decision drivers that executives should keep in mind when it comes retaining a lawyer with a job offer from a rival?
- which are the lawyers that should be retained by matching any offer coming from rivals? Why?

# Data

## Source

Data have been collected using a digital survey circulated among associate lawyers and their supervisors. The number of respondents is 817.

## Data tables

The dataset contains two types of data: attributive data on associate lawyers and inter-personal interactions among associate lawyers.

Attributive data (see `attributive_data.csv`) comprise the following variables:

+ `org_tnr`: years spent at ⍺βƔ (from internal archive; z-scores reported)
+ `prf`: individual performance (based on supervisor ratings). The measure, expressed as a z-score, takes into account both effectiveness and efficiency
+ `ocb`: individual [organizational citizenship behavior (OCB)](https://en.wikipedia.org/wiki/Organizational_citizenship_behavior) (based on supervisor ratings). The measure, expressed as a z-score, comes from the prior literature on OCB[3]
+ `ldr`: individual ability/capacity to project his/her view and to guide others' behavior over and beyond roles and organizational/reporting structures (based on supervisor ratings). The measure, expressed as a z-score, comes from the prior literature on charismatic leadership[4]

Relational data (`.gml` format):

+ `knw_exc.gml`: a one mode-network expressing who is exchanging knowledge with whom. By knowledge, the survey means mental models and schemas that help individuals to carry out projects and to navigate the complexity of the organization they belong to. Note these mental models and schemas are informal, that is, not codified in any organizational procedure

# References

[1] Barney, J. (1991). [Firm resources and sustained competitive advantage](https://journals.sagepub.com/doi/pdf/10.1177/014920639101700108?casa_token=ScA0C5HlXjcAAAAA:y4nF8MG3_rD9aNxoyFcYdr6h4S5ZwLJaTxG_DbSEZobn8mkJyYd4wP0I2Qn9GK9W6q70pwjjME9G). _Journal of Management_, 17(1), 99-120.

[2] Dess, G. G., & Shaw, J. D. (2001). [Voluntary turnover, social capital, and organizational performance](https://www.researchgate.net/profile/Jason_Shaw5/publication/272581384_Voluntary_Turnover_Social_Capital_and_Organizational_Performance/links/551161db0cf29a3bb71da8db.pdf). _Academy of Management Review_, 26(3), 446-456.

[3] Podsakoff, P. M., MacKenzie, S. B., Moorman, R. H., & Fetter, R. (1990). [Transformational leader behaviors and their effects on followers' trust in leader, satisfaction, and organizational citizenship behaviors](https://www.academia.edu/download/32225715/Transformational_Leader_Behavior_Podsakoff_et_al.pdf). _The Leadership Quarterly_, 1(2), 107-142.

[4] O'Connor, J., Mumford, M. D., Clifton, T. C., Gessner, T. L., & Connelly, M. S. (1995). [Charismatic leaders and destructiveness: An historiometric study](https://www.sciencedirect.com/science/article/pii/1048984395900268). The Leadership Quarterly, 6(4), 529-555.
