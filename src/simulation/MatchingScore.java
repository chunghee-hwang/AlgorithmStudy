package src.simulation;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
//https://programmers.co.kr/learn/courses/30/lessons/42893
public class MatchingScore {
    private LinkedList<Site> sites = new LinkedList<>();
    private HashMap<String, Site> siteMap = new HashMap<>();

    private static class Site{
        String link;
        String page;
        LinkedList<String> outLinks = new LinkedList<>();
        int defaultScore;
        int outLinkCnt;
        double linkScore;
        double matchingScore;
        int idx;
        Site(int idx, String link, String page){
            this.idx = idx;
            this.link = link;
            this.page = page;
        }
        private void computeMatchingScore(){
            matchingScore = defaultScore+linkScore;
        }
        private void addLinkScore(Site otherSite){
            linkScore += otherSite.defaultScore/(double)otherSite.outLinkCnt;
        }
    }

    private void registerSite(String page, int idx) {
        Pattern p = Pattern.compile("<head>.+</head>");
        Matcher m = p.matcher(page);
        if (m.find()) {
            String headPart = m.group();
            p = Pattern.compile("<meta property=\"og:url\" content=\"https://\\S+\"|<meta content=\"https://\\S+\" property=\"og:url\"");
            m = p.matcher(headPart);
            if (m.find()) {
                String link = m.group().replaceAll("\"|<meta property=\"og:url\"|content=|\\s", "");
                Site site = new Site(idx, link, page);
                sites.add(site);
                siteMap.put(link, site);
            }
        }
    }


    private void analyzeWordAndLink(String word, Site curSite) {
        String page = curSite.page;
        String exceptAlphabet = "[\\W|\\d]";
        String removed = page.replaceAll(exceptAlphabet, " ");
        Pattern p = Pattern.compile("\\b"+word+"\\b");
        Matcher m = p.matcher(removed);
        int defaultScore = 0;
        int outLinkCnt = 0;
        while (m.find()) {
            defaultScore++;
        }
        curSite.defaultScore = defaultScore;
        p = Pattern.compile("<a href=\"https://\\S+\"");
        m = p.matcher(page);
        while (m.find()) {
            String outLink = m.group().replaceAll("\"|<a href=", "");
            curSite.outLinks.add(outLink);
            outLinkCnt++;
        }
        curSite.outLinkCnt = outLinkCnt;
    }

    private void analyzeOutLink(Site curSite){
        for (String outLink : curSite.outLinks) {
            Site otherSite = siteMap.get(outLink);
            if(otherSite!=null) otherSite.addLinkScore(curSite);
        }
    }
    public int solution(String word, String[] pages) {
        int n = pages.length;
        word = word.toLowerCase();
        for(int i = 0; i <n; i++){
            pages[i] = pages[i].toLowerCase().replaceAll("[\n]", " ");
        }
        for(int i =0; i<n;i++){
            registerSite(pages[i],i);
        }
        for (Site site : sites) {
            analyzeWordAndLink(word, site);
        }

        for (Site site : sites) {
            analyzeOutLink(site);
        }
        for (Site site : sites) {
            site.computeMatchingScore();
        }
        if(sites.size() > 0) {
            sites.sort((o1, o2) -> {
                double score1 = o1.matchingScore;
                double score2 = o2.matchingScore;
                if(score1 != score2) {
                    return Double.compare(score2, score1);
                }
                return o1.idx - o2.idx;
            });
            return sites.get(0).idx;
        }
        else return -1;
    }


    public static void main(String[] args) {
        String[] word = {"<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"
        };
        System.out.println(new MatchingScore().solution("Muzi", word));
    }
}