n = int(input())

Triangle = {
    1: "    *\n" +
       "   * *\n" +
       "  *   *\n" +
       " *     *\n" +
       "*********",

    2: "    *\n" +
       "   ***\n" +
       "  *****\n" +
       " *******\n" +
       "*********",

    3: "*********\n" +
       " *******\n" +
       "  *****\n" +
       "   ***\n" +
       "    *"
}

print(Triangle[n])
