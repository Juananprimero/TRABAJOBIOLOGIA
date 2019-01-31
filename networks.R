if(getwd()!="~/Desktop/IS/4º/1er_cuatri/Biología de sistemas/Trabajo"){
  setwd("~/Desktop/IS/4º/1er_cuatri/Biología de sistemas/Trabajo")
}

library(dplyr)
library(ggplot2)
library(igraph)
library(ggraph)

data <- read.csv(file='drug_targetV2.csv', sep = ',', header = TRUE)
data <- dplyr::arrange(data, desc(pchembl_value))
head(data)
d.data <- distinct(data, drug, target, .keep_all = TRUE)
head(d.data)
d.data <- dplyr::filter(d.data, drug == 'ESTRADIOL' | drug == 'DIETHYLSTILBESTROL' | drug == 'TAMOXIFEN' | drug == 'MIFEPRISTONE')
#write.csv2(d.data, file='drug_targetV2_procesed.csv', sep = ',')

mygraph <- graph_from_data_frame(d = d.data)
set.seed(1)

pdf(file = "interactionsV3.pdf")
ggraph(mygraph) +
  geom_edge_link(aes(end_cap = circle(radius = 2, unit = "mm"),
                     color = pchembl_value, alpha = pchembl_value, edge_width = pchembl_value),
                 arrow = arrow(type = "open", length = unit(3, "mm")),
                 show.legend = FALSE) +
  scale_edge_color_continuous(low = "#666666", high = "#00ccaa") +
  scale_edge_width(range = c(.01, 1.3)) +
  scale_edge_alpha(range = c(.6, 1)) +
  geom_node_point(size = 1) +
  geom_node_text(aes(label = name), repel = TRUE) + 
  theme_void()
dev.off()
