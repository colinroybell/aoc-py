from utils.day_base import DayBase
from utils.data_input import input_generator
from utils.vec_3d import Vec3d
from math import log
from fractions import Fraction

class Run_2023_24(DayBase):
    YEAR = "2023"
    DAY = "24"


from itertools import combinations
def part1(data):
    valid = 0
    imin, imax = 200_000_000_000_000, 400_000_000_000_000
    #imin, imax = 7, 27
    print(data)
    for l1, l2 in combinations(data, 2):
        xp1, yp1, _, xv1, yv1, _ = l1
        xp2, yp2, _, xv2, yv2, _ = l2


        if yv1*xv2 == yv2*xv1:
            continue
        t1 = (yv2*(xp1-xp2) - xv2*(yp1-yp2))/(yv1*xv2 - xv1*yv2)
        t2 = (yv1*(xp2-xp1) - xv1*(yp2-yp1))/(yv2*xv1 - xv2*yv1)
        if t1 < 0 or t2 < 0:
            continue
        ix = xp1 + t1*xv1
        iy = yp1 + t1*yv1

        print(ix,iy)

        if imin <= ix <= imax and imin <= iy <= imax:
            valid += 1
    return valid

import sympy as sym

def part2(stones):
    p = [stones[0][0],stones[1][0],stones[2][0]]
    v = [stones[0][1],stones[1][1],stones[2][1]]
    rpx, rpy, rpz, rvx, rvy, rvz, t0, t1, t2 = sym.symbols("rpx, rpy, rpz, rvx, rvy, rvz, t0, t1, t2")
    eqs = [sym.Eq(rpx + rvx * t0, p[0].x + t0 * v[0].x),
           sym.Eq(rpy + rvy * t0, p[0].y + t0 * v[0].y),
           sym.Eq(rpz + rvz * t0, p[0].z + t0 * v[0].z),
           sym.Eq(rpx + rvx * t1, p[1].x + t1 * v[1].x),
           sym.Eq(rpy + rvy * t1, p[1].y + t1 * v[1].y),
           sym.Eq(rpz + rvz * t1, p[1].z + t1 * v[1].z),
           sym.Eq(rpx + rvx * t2, p[2].x + t2 * v[2].x),
           sym.Eq(rpy + rvy * t2, p[2].y + t2 * v[2].y),
           sym.Eq(rpz + rvz * t2, p[2].z + t2 * v[2].z)]
    s = sym.solve(eqs, [rpx, rpy, rpz, rvx, rvy, rvz, t0, t1, t2])[0]
    print(s)
    return s[0]+s[1]+s[2]



def line_intersect(p1, q1, p2, q2):
    v1 = q1 - p1
    v2 = q2 - p2
    divisor = v1.x * v2.y - v1.y * v2.x
    if divisor == 0:
        print(v1,v2)
        print("Parallel")
        return None
    t = ((p2.x-p1.x) * v2.y - (p2.y-p1.y) * v2.x)/divisor
    u = ((p2.x-p1.x) * v1.y - (p2.y-p1.y) * v1.x)/divisor

    if t < 0 or u < 0:
        print("Past",t,u)
        return None

    int_point = p1 + v1 * t # How to define it other way round?
    print('t',t,'u',u)
    return (int_point,t,u)

def project(p):
    assert p.z
    return Vec3d(Fraction(p.x,p.z),Fraction(p.y,p.z), Fraction(1))
    #return Vec3d(p.x/p.z,p.y/p.z,1)

from re import findall

def part_a(input, test_min = 200000000000000, test_max = 400000000000000):
    print(test_min, test_max)
    #test_min = 7
    #test_max = 27
    stones = []
    for line in input_generator(input):
        (pos_s,vel_s) = line.split('@')
        p = pos_s.split(',')
        print(p)
        p_v = Vec3d(int(p[0]),int(p[1]),int(p[2]))
        v = vel_s.split(',')
        v_v = Vec3d(int(v[0]),int(v[1]),int(v[2]))
        stones.append((p_v,v_v))

    count = 0
    for i,s1 in enumerate(stones):
        for j,s2 in enumerate(stones[i+1:]):
            print(s1,s2)
            (p1,v1) = s1
            (p2,v2) = s2
            divisor = v1.x * v2.y - v1.y * v2.x
            if divisor == 0:
                print("Parallel")
                continue
            t = ((p2.x-p1.x) * v2.y - (p2.y-p1.y) * v2.x)/divisor
            u = ((p2.x-p1.x) * v1.y - (p2.y-p1.y) * v1.x)/divisor

            if t < 0 or u < 0:
                print("Past")
                continue

            int_point = p1 + v1 * t # How to define it other way round?
            print (int_point)
            if test_min <= int_point.x <= test_max and test_min <= int_point.y<=test_max:
                count += 1

    return count

def part_b(input):
    stones = []
    for line in input_generator(input):
        (pos_s,vel_s) = line.split('@')
        p = pos_s.split(',')
        #print(p)
        p_v = Vec3d(int(p[0]),int(p[1]),int(p[2]))
        v = vel_s.split(',')
        v_v = Vec3d(int(v[0]),int(v[1]),int(v[2]))
        stones.append((p_v,v_v))

    return part2(stones)

    for target in range(len(stones)):

        (p0,v0) = stones[target]
        base = p0 + v0

        print(target, 'base', base)

        first = True
        ref_ip = None
        failed = False
        for i,s1 in enumerate(stones):
            if i == target:
                continue
            for j,s2 in enumerate(stones):
                if j == target or j<=i:
                    continue
                (p1,v1) = stones[i]
                (p2,v2) = stones[j]

                p1 = p1 + v1 - base
                p2 = p2 + v2 - base
                q1 = p1 + v1
                q2 = p2 + v2
                print(i,j)
                #print(p1,q1,p2,q2)
                pp1 = project(p1)
                pp2 = project(p2)
                pq1 = project(q1)
                pq2 = project(q2)
                #print(pp1,pq1,pp2,pq2)

                intersect = line_intersect(pp1,pq1,pp2,pq2)
                if intersect:
                    ip = intersect[0]
                    print(ip)
                    if first:
                        ref_ip = ip
                        first = False
                    else:
                        if ref_ip != ip:
                            failed = True
                            break
            if failed:
                break
        if not failed and not first:
            print("Success: ", ref_ip)
            for i,s1 in enumerate(stones):
                (p1,v1) = s1

                (ip2,t,u) = line_intersect(Vec3d(0,0,0),ip,p1-base,p1-base+v1)
                print (ip2,t,u)
                int_u = int(u+0.5)
                print ('Final', i,int(u+0.5))
                if u > 1:
                    pos = base - ip2/(u-1)
                    print('pos')
                    return int(pos.x+pos.y+pos.z+0.5)






if __name__ == "__main__":
    Run_2023_24().run_cmdline()
