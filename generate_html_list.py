def generate_html_list(data):
    html = "<ul>\n"
    for entry in data:
        
        html += f"<li>{entry}</li>\n"
    html += "</ul>"
    return html

def main():
    data = ["John Doe, VU Amsterdam", "Alice Smith, University of California, Santa Cruz"]
    

    data = ["Ada Gavrilovska, Georgia Tech",
"Adil Ahmad, Arizona State University",
"Alain Tchana, Grenoble INP",
"Andreas Schmidt, Saarland University",
"Anjo Vahldiek-Oberwagner, Intel Labs",
"Antoine Kaufmann, Max Plank Institute for Software Systems (MPI-SWS)",
"Anton Burtsev, University of Utah",
"Antonio Barbalace, The University of Edinburgh",
"Anurag Khandelwal, Yale University",
"Ashvin Goel, University of Toronto",
"Baptiste Lepers, The University of Neuchâtel",
"Beomseok Nam, Sungkyunkwan University",
"Boris Grot, University of Edinburgh, Huawei Research",
"Călin Iorgulescu, Oracle Labs",
"Chang Lou, University of Virginia",
"Cheng Li, University of Science and Technology of China",
"Cheng Tan, Northeastern University",
"Chia-Che Tsai, Texas A&M University",
"Christian Dietrich, Hamburg University of Technology",
"Cristina Nita-Rotaru, Northeastern University",
"Dan Williams, Virginia Tech",
"Daniel Lohmann, Leibniz Universität Hannover",
"Diogo Behrens, Huawei",
"Donald Porter, The University of North Carolina at Chapel Hill",
"Emmanuel Baccelli, Inria",
"Emmanuel Cecchet, University of Massachusetts Amherst",
"Etienne Rivière, UCLouvain",
"Fan Lai, UIUC",
"Fan Yang, Microsoft Research Asia",
"Gaël Thomas, Inria Saclay",
"Haifeng Yu, National University of Singapore",
"Horst Schirmeier, TU Dresden",
"Hyungon Moon, UNIST",
"Indrajit Roy, Google Inc",
"Jacob Gorm Hansen, Jamscape",
"Jayashree Mohan, Microsoft Research",
"Jean-Pierre Lozi, Inria",
"Jeff Mogul, Google",
"Jia-Ju Bai, Beihang University",
"Jialin Li, National University of Singapore",
"Jian Huang, UIUC",
"John Wilkes, Google",
"Jon Crowcroft, University of Cambridge",
"Kai Chen, Hong Kong University of Science and Technology",
"Kang Chen, Tsinghua University",
"Keval Vora, Simon Fraser University",
"Laiping Zhao, TianJin University",
"Larry Rudolph, Two Sigma Investments, LP",
"Laurent Bindschaedler, Max Planck Institute for Software Systems",
"Liuba Shrira, Brandeis University",
"Luo Mai, University of Edinburgh",
"Malte Schwarzkopf, Brown University",
"Mangpo Phothilimthana, Google DeepMind",
"Marc Shapiro, Sorbonne-Université–LIP6 & Inria",
"Marco Serafini, University of Massachusetts Amherst",
"Maria Carpen-Amarie, Huawei Research",
"Martin Kleppmann, University of Cambridge",
"Matteo Interlandi, Microsoft",
"Michael Swift, University of Wisconsin-Madison",
"Michio Honda, University of Edinburgh",
"Djob Mvondo, Univ Rennes, CNRS, INRIA, IRISA",
"Nuno Preguica, Universidade Nova de Lisboa",
"Olaf Spinczyk, Osnabrueck University",
"Patrick P. C. Lee, The Chinese University of Hong Kong",
"Philippe Bonnet, DIKU",
"Pierre Olivier, The University of Manchester",
"Pramod Bhatotia, Technical University of Munich",
"Qian Ge, Google DeepMind",
"Redha Gouicem, RWTH Aachen University",
"Renaud Lachaize, Université Grenoble Alpes",
"Reto Achermann, University of British Columbia",
"Rishabh Iyer, UC Berkeley",
"Roberto Natella, University of Naples Federico II",
"Rong Chen, Shanghai Jiao Tong University",
"Sam H. Noh, Virginia Tech",
"Sanidhya Kashyap, EPFL",
"Sara Hamouda, Google",
"Serdar Tasiran, Amazon Web Services",
"Shimin Chen, ICT, CAS & University of Chinese Academy of Sciences",
"Shuai Mu, Stony Brook University",
"Soujanya Ponnapalli, UC Berkeley",
"Steve Blackburn, Google",
"Thaleia Dimitra Doudali, IMDEA Software Institute",
"Tim Harris, Microsoft",
"Timo Hönig, Ruhr-Universität Bochum (RUB)",
"Tobias Distler, FAU Erlangen-Nürnberg",
"Trinabh Gupta, UCSB",
"Valerio Schiavoni, University of Neuchatel",
"Vero Estrada-Galiñanes, EPFL",
"Wenguang Chen, Tsinghua University",
"Wenjun Hu, Yale University",
"Xiaosong Ma, Qatar Computing Research Institute",
"Y. Charlie Hu, Purdue University",
"Yang Wang, Meta/The Ohio State University",
"Yanyan Jiang, Nanjing University",
"Yérom-David Bromberg, University of Rennes, INRIA",
"Yizhou Shan, Huawei Cloud",
"Yongle Zhang, Purdue",
"Youngjin Kwon, KAIST",
"Youyou Lu, Tsinghua University",
"Yu Hua, Huazhong University of Science and Technology",
"Yu Liang, ETH Zurich",
"Yubin Xia, Shanghai Jiao Tong University",
"Yuvraj Patel, University of Edinburgh",
"Zhaoguo Wang, Shanghai Jiao Tong University",
"Zsolt István, TU Darmstadt"]
    
    html_list = generate_html_list(data)
    with open("output.html", "w") as file:
        file.write(html_list)
    print("HTML list generated successfully!")

if __name__ == "__main__":
    main()