class MyHashMap {

    class Pair {
        int key;
        int value;

        Pair(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    int size = 1000;
    LinkedList<Pair>[] map;

    public MyHashMap() {
        map = new LinkedList[size];

        for (int i = 0; i < size; i++) {
            map[i] = new LinkedList<>();
        }
    }

    private int hash(int key) {
        return key % size;
    }
    
    public void put(int key, int value) {
        int index = hash(key);

        for (Pair p : map[index]) {
            if (p.key == key) {
                p.value = value; // update existing key
                return;
            }
        }

        map[index].add(new Pair(key, value));
    }
    
    public int get(int key) {
        int index = hash(key);

        for (Pair p : map[index]) {
            if (p.key == key) {
                return p.value;
            }
        }

        return -1;
    }
    
    public void remove(int key) {
        int index = hash(key);

        Iterator<Pair> it = map[index].iterator();

        while (it.hasNext()) {
            Pair p = it.next();

            if (p.key == key) {
                it.remove();
                return;
            }
        }
    }
}