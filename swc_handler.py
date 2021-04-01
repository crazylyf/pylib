"""*================================================================
*   Copyright (C) 2021 Yufeng Liu (Braintell, Southeast University). All rights reserved.
*   
*   Filename    : swc_handler.py
*   Author      : Yufeng Liu
*   Date        : 2021-03-15
*   Description : 
*
================================================================*"""

def parse_swc(swc_file):
    tree = []
    with open(swc_file) as fp:
        fp.readline() # skip the header line
        for line in fp.readlines():
            line = line.strip()
            if not line: continue
            idx, type_, x, y, z, r, p = line.split()
            idx = int(idx)
            type_ = int(type_)
            x = float(x)
            y = float(y)
            z = float(z)
            r = float(r)
            p = int(p)
            tree.append((idx, type_, x, y, z, r, p))
    
    return tree

def write_swc(tree, swc_file):
    with open(swc_file, 'w') as fp:
        fp.write(f'##n type x y z r parent\n')
        for leaf in tree:
            idx, type_, x, y, z, r, p = leaf
            fp.write(f'{idx:d} {type_:d} {x:.2f} {y:.2f} {z:.2f} {r:.1f} {p:d}\n')
    

