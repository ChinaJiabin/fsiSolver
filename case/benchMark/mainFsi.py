import sys
sys.path.append("/home/jiabin/python/lan/")
import lanFsi

def main(argv):

    fsiAlgorithm=lanFsi.fsiAlgorithm()
    fsiAlgorithm.IQN_ILS(5)

if __name__ == '__main__':
   main(sys.argv)

