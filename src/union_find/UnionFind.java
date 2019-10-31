package union_find;

//합집합 찾기
public class UnionFind {

    //부모를 찾는 함수
    private static int findParent(int []parent, int x){
        if(parent[x] == x) return x;
        return parent[x] = findParent(parent, parent[x]);
    }

    //각 부모 노드를 합칩니다.
    private static void unionParent(int []parent, int a, int b){
        a = findParent(parent, a);
        b = findParent(parent, b);
        if(a < b) parent[b] = a;
        else parent[a] = b;
    }

    //두 노드의 부모가 같은지 확인합니다.
    private static boolean isSameParent(int []parent, int a, int b){
        return findParent(parent, a) == findParent(parent, b);
    }

    public static void main(String[] args) {
        int []parent = new int[11]; //10개의 노드
        for(int i = 1; i <=10; i++){
            parent[i] = i;
        }

        unionParent(parent, 1,2);
        unionParent(parent, 2,3);
        unionParent(parent, 3,4);
        unionParent(parent, 5,6);
        unionParent(parent, 7,8);
        System.out.println("1과 5는 연결되어있나요? "+isSameParent(parent,1,5));
        unionParent(parent,1,5);
        System.out.println("1과 5는 연결되어있나요? "+isSameParent(parent,1,5));
    }

}
