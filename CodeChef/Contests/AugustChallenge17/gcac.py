#!/usr/bin/env python3

# O(N*M)

def main():
    T = int(input())
    for _ in range(T):
        N,M = map(int,input().split())
        minSalary = list(map(int,input().split()))
        offeredSalary = [0]*M  # they will be distinct
        maxJobOffers = [0]*M
        for i in range(M):
            offeredSalary[i],maxJobOffers[i] = map(int,input().split())
        qual = []
        for _ in range(N):
            qual.append([c=='1' for c in input()])
        jobOffers = [0]*M
        for i in range(N):
            bestj = None
            for j in range(M):
                if qual[i][j] and offeredSalary[j]>=minSalary[i] and jobOffers[j]<maxJobOffers[j]:
                    if bestj==None or offeredSalary[j]>offeredSalary[bestj]:
                        bestj = j
            if bestj!=None:
                jobOffers[bestj] += 1
        nbJobs = sum(jobOffers)
        salSum = sum(jobOffers[j]*offeredSalary[j] for j in range(M))
        badComp = jobOffers.count(0)
        print(nbJobs,salSum,badComp)

main()
