package test.위메프;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

class Solution3 {

    private static class Product{
        int weight;
        boolean selected;
        Product(int w){
            weight = w;
        }
    }

    private static long getUnselectedProductsCount(List<Product> products){
        return products.stream().filter(p -> !p.selected).count();
    }

    private static int selectProducts(List<Product> products, int maxWeight){
        if(getUnselectedProductsCount(products) == 0) return 1;
        List<Product> unselected =
                products.stream()
                .filter(p -> !p.selected)
                .sorted((o1, o2) -> o2.weight - o1.weight)
                .collect(Collectors.toList());
        int sum = 0;
        for(Product p : unselected){
            if(sum + p.weight <= maxWeight){
                sum+= p.weight;
                p.selected = true;
            }
            if(sum == maxWeight)
                break;
        }
        if(sum == 0){
            return -1;
        }
        return 0;
    }

    public static void main(String[] args) {
        int weight = 200;
        int productLength = 12;
        int []products = {58, 70, 54, 85, 99, 125, 100, 75, 76, 80, 88, 75};
        ArrayList<Product> list = new ArrayList<>();
        list.add(new Product(58));
        list.add(new Product(70));
        list.add(new Product(54));
        list.add(new Product(85));
        list.add(new Product(99));
        list.add(new Product(125));
        list.add(new Product(201));
        list.add(new Product(75));
        list.add(new Product(76));
        list.add(new Product(80));
        list.add(new Product(88));
        list.add(new Product(75));

        int result;
        int cnt = 0;
        while((result = selectProducts(list, weight)) == 0){
            cnt++;
        }
        if(result == 1) System.out.println(cnt);
        else System.out.println(result);
    }
}