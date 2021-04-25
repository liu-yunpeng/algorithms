def findRedundantDirectedConnection(edges: Array[Array[Int]]): Array[Int] = {
  val count = edges.flatten.toSet.size
  def stillConnected(i: (Int, Int), g: Map[Int, Set[Int]]): Boolean = {
    def dfs(n: Int, visited: Set[Int]): Set[Int] =
      g(n).foldLeft(visited) {
        case (v, x) if !v.contains(x) => dfs(x, v + x)
        case (v, _) => v
      }
    val root = g.keySet -- g.values.flatten
    root.size == 1 && dfs(root.head, root).size == count
  }
  val graph = edges.foldLeft(Map[Int, Set[Int]]().withDefaultValue(Set.empty)) {
    case (map, Array(s, e)) => map.updated(s, map(s) + e)
  }
  edges.reverse.find {
    case Array(s, e) => stillConnected((s, e), graph.updated(s, graph(s) - e))
  }.get
}