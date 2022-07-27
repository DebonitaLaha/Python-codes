if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name =input().strip()
    s=0.00
    if student_marks.get(query_name) == student_marks[query_name]:
         for j in student_marks[query_name]:
            s=s+j
    d=s/3
    print ("Value: %.2f" % float(d))