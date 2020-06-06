# https://projecteuler.net/problem=8


def naiveApproach(digits):
    """Iterate through the numbers and create combinations of adjacent numbers of the size mentioned in digits. This
    uses the sliding window approach and has time complexity of O(N*M) where N is number size and M is the
    consecutive digits size """

    # the 1000 digits number
    num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858" \
          "6156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966" \
          "4895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072" \
          "9629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010" \
          "5336788122023542180975125454059475224352584907711670556013604839586446706324415722155397536978179778461" \
          "7406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844031998" \
          "9000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294" \
          "7654568284891288314260769004224219022671055626321111109370544217506941658960408071984038509624554443629" \
          "8123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050775410022" \
          "5698315520005593572972571636269561882670428252483600823257530420752963450"
    
    max_product = 1

    for i in range(len(num)):
        product = 1

        for d in range(i, i + digits):
            if d < len(num):
                product *= int(num[d])
            else:
                break

        if product > max_product:
            max_product = product

    return max_product


if __name__ == "__main__":
    print(naiveApproach(4))  # 5832
    print(naiveApproach(13))  # 23514624000
