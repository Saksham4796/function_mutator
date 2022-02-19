import re

source_code = open("sample.c").read().split('\n')
number_of_lines_of_code = len(source_code)
#print number_of_lines_of_code

def get_line_index(m,n):
	op = 1 
	cl = 0
	for i in range(m+1,number_of_lines_of_code):
		l = len(source_code[i])
		for j in range(l):
			if source_code[i][j] == '{' :
				op = op + 1				
			elif source_code[i][j] == '}' :
				cl = cl + 1				
				if op == cl :				
					return [i,j]

lst = []
for i in range(number_of_lines_of_code):
	if source_code[i].find("calculate_outputm") != -1 and source_code[i].find(';') != -1 :
		temp = re.findall(r'\d+', source_code[i])
		func_num = list(map(int,temp))[0]
		if func_num not in lst :
			lst.append(func_num)
print lst

z = 1 

with open("log.txt",'w') as lf :

	for i in range(number_of_lines_of_code):
		if source_code[i].find("void calculate_output(int input)") != -1 and source_code[i].find(';') == -1 :
			open_brace_index = source_code[i].find('{')
			close_brace_line = get_line_index(i,open_brace_index)[0]
			close_brace_index = get_line_index(i,open_brace_index)[1]
			for j in range(i+1,close_brace_line):
				print j
				if source_code[j].find("calculate_outputm") != -1:
					temp = re.findall(r'\d+', source_code[j])
					func_num = list(map(int,temp))[0]
					#print func_num
					for l in lst :
						
						if l != func_num : 
						
							output_file = open("sample_m"+str(z)+".c","w")
									
							for p in range(0,len(source_code)) :

								if p == j : 
									line = source_code[p].replace(str(func_num),str(l))
									lf.write("Mutant m"+str(z)+'\n\n')
									lf.write("Line no. : "+str(j)+'\n')
									lf.write("Original Line: "+source_code[j]+'\n')
									lf.write("Manipulated Line: "+line+'\n\n\n')
									#print (line,p)
									output_file.write(line+"\n")
								else :
									output_file.write(source_code[p]+"\n")

							output_file.close()
							z = z + 1

		elif source_code[i].find("int main()") != -1 and source_code[i].find(';') == -1 :
			
			open_brace_index = source_code[i].find('{')
			close_brace_line = get_line_index(i,open_brace_index)[0]
			close_brace_index = get_line_index(i,open_brace_index)[1]		
			for j in range(i+1,close_brace_line):
				print j
				if source_code[j].find("calculate_output") != -1:

					for l in lst:

						output_file = open("sample_m"+str(z)+".c","w")
									
						for p in range(0,len(source_code)) :

							if p == j : 
								line = source_code[p].replace("calculate_output","calculate_outputm"+str(l))
								lf.write("Mutant m"+str(z)+'\n\n')
								lf.write("Line no. : "+str(j)+'\n')
								lf.write("Original Line: "+source_code[j]+'\n')
								lf.write("Manipulated Line: "+line+'\n\n\n')
								#print (line,p)
								output_file.write(line+"\n")
							else :
								output_file.write(source_code[p]+"\n")

						output_file.close()
						z = z + 1

lf.close()

print z

		 		 
