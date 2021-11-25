import {
  createSlice,
  createSelector,
  PayloadAction,
} from "@reduxjs/toolkit";

import { RootState, StoreDispatch, StoreGetState } from '../configureStore';

export interface Menu {
  id: number;
  name: string;
  way: string;
  pat: string;
  energy: number;
  carb: number;
  protein: number;
  fat: number;
  na: number;
  hashtag: string;
  img_small: string;
  img_large: string;
  ingredients_count: number;
}

export interface ForceMenu{
  size: number
}

export interface Ingredient {
  id: number;
  name: string;
  count: number;
}

export interface Recipe {
  order: number;
  text: string;
  img: string;
}

export interface MenuDetail extends Menu {
  ingredients: string;
  ingredients_set: Array<Ingredient>;
  recipes: Array<Recipe>;
}

export interface IngredientDetail extends Ingredient {
  menus: Array<Menu>;
}

export type ValueCountTuple = [string, number];

export interface DataState {
  flagLoadData?: boolean;
  menus?: Menu[];
  ingredients?: Ingredient[];
  ways?: ValueCountTuple[];
  pats?: ValueCountTuple[];
  hashtags?: ValueCountTuple[];
}

export const initialDataState: DataState = {
  flagLoadData: true,
};

export const getPreloadedDataState = (): DataState => {
  return {
    ...initialDataState,
  };
};

const slice = createSlice({
  name: "data",
  initialState: initialDataState,
  reducers: {
    loadData: (state) => {
      state.flagLoadData = true;
    },
    doneLoadingData: (state) => {
      state.flagLoadData = false;
    },
    setMenus: (state, action: PayloadAction<Menu[]>) => {
      state.menus = action.payload;
    },
    setIngredients: (state, action: PayloadAction<Ingredient[]>) => {
      state.ingredients = action.payload;
    },
    setWays: (state, action: PayloadAction<ValueCountTuple[]>) => {
      state.ways = action.payload;
    },
    setPats: (state, action: PayloadAction<ValueCountTuple[]>) => {
      state.pats = action.payload;
    },
    setHashtags: (state, action: PayloadAction<ValueCountTuple[]>) => {
      state.hashtags = action.payload;
    },
  },
});

const { reducer } = slice;

export const {
  loadData,
  doneLoadingData,
  setMenus,
  setIngredients,
  setWays,
  setPats,
  setHashtags,
} = slice.actions;

export const selectMenus = createSelector(
  (state: RootState) => state.data.menus,
  (menus) => menus
);
export const selectIngredients = createSelector(
  (state: RootState) => state.data.ingredients,
  (ingredients) => ingredients
);
export const selectWays = createSelector(
  (state: RootState) => state.data.ways,
  (ways) => ways
);
export const selectPats = createSelector(
  (state: RootState) => state.data.pats,
  (pats) => pats
);
export const selectHashtags = createSelector(
  (state: RootState) => state.data.hashtags,
  (hashtags) => hashtags
);

export default reducer;