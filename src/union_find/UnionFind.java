package union_find;

//합집합 찾기
public class UnionFind {

    //부모를 찾는 함수
    private int findParent(int []parent, int x){
        if(parent[x] == x) return x;
        return parent[x] = findParent(parent, parent[x]);
    }

    //각 부모 노드를 합칩니다.
    private void unionParent(int []parent, int a, int b){
        a = findParent(parent, a);
        b = findParent(parent, b);
        if(a < b) parent[b] = a;
        else parent[a] = b;
    }

    //두 노드의 부모가 같은지 확인합니다.
    private boolean isSameParent(int []parent, int a, int b){
        return findParent(parent, a) == findParent(parent, b);
    }
}
