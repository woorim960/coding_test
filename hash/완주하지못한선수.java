import java.util.HashMap;
import java.util.Map;
import static java.util.stream.Collectors.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> playerCnts = getPlayerCnts(participant, completion);
        String notCompletionPlayer = getNotCompletionPlayer(playerCnts);
        return notCompletionPlayer;
    }
    
    public HashMap<String, Integer> getPlayerCnts(String[] participant, String[] completion) {
        HashMap<String, Integer> playerCnts = new HashMap<>();
        playerCnts = getParticipantCnts(participant);
        playerCnts = getCompletionCnts(completion, playerCnts);
        return playerCnts;
    }
    
    public HashMap<String, Integer> getParticipantCnts(String[] participant) {
        HashMap<String, Integer> participantCnts = new HashMap<>();
        for (String player: participant) {
            if (participantCnts.containsKey(player)) {
                participantCnts.put(player, participantCnts.get(player) + 1);
                continue;
            }
            participantCnts.put(player, 1);
        }
        return participantCnts;
    }
    
    public HashMap<String, Integer> getCompletionCnts(String[] completion, HashMap<String, Integer> playerCnts) {
        HashMap<String, Integer> completionCnts = new HashMap<>(playerCnts);
        for (String player: completion) {
            completionCnts.put(player, completionCnts.get(player) - 1);
        }
        return completionCnts;
    }
    
    public String getNotCompletionPlayer(HashMap<String, Integer> playerCnts) {
        Map<String, Integer> playerCnt = 
            playerCnts.entrySet()
                .stream()
                .filter(player -> player.getValue().equals(1))
                .collect(toMap(player -> player.getKey(), player -> player.getValue()));
        return playerCnt.keySet().iterator().next();
    }
}
