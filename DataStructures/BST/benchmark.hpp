class BSTStructure {
public:
  virtual bool exists(int x) = 0;
  virtual void insert(int x) = 0;
  virtual void erase(int x) = 0;
  virtual void clear() = 0;
};

void bench(BSTStructure *S);
